from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User

from .models import Follow
from .models import FollowRequest
from .serializers import FollowRequestSerializer
from .serializers import FollowSerializer


class FollowRequestViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        follow_requests = FollowRequest.objects.filter(
            sender=user
        ) | FollowRequest.objects.filter(receiver=user)
        serializer = FollowRequestSerializer(follow_requests, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            follow_request = FollowRequest.objects.get(pk=pk)
            serializer = FollowRequestSerializer(follow_request)
            return Response(serializer.data)
        except FollowRequest.DoesNotExist:
            return Response(
                {"error": "Follow request not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["post"], url_path="send-follow-request")
    def send_follow_request(self, request, *args, **kwargs):
        sender = request.user
        receiver_id = kwargs.get("pk")

        try:
            receiver = User.objects.get(pk=receiver_id)
        except User.DoesNotExist:
            return Response(
                {"error": "Receiver not found"}, status=status.HTTP_404_NOT_FOUND
            )

        data = {"sender": sender.id, "receiver": receiver.id}
        context = {"request": request}

        serializer = FollowRequestSerializer(data=data, context=context)

        if serializer.is_valid():
            follow_request = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_path="accept-follow-request")
    def accept_follow_request(self, request, *args, **kwargs):
        follow_request_id = kwargs.get("pk")

        try:
            follow_request = FollowRequest.objects.get(pk=follow_request_id)
        except FollowRequest.DoesNotExist:
            return Response(
                {"error": "Follow request does not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = {"status": "accepted"}
        serializer = FollowRequestSerializer(follow_request, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            follower = follow_request.sender_id
            following = follow_request.receiver_id

            data = {"follower": follower, "following": following}

            follow_serializer = FollowSerializer(data=data)

            if follow_serializer.is_valid():
                follow_serializer.save()
                return Response(follow_serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(
                    follow_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_path="decline-follow-request")
    def decline_follow_request(self, request, *args, **kwargs):
        follow_request_id = kwargs.get("pk")

        try:
            follow_request = FollowRequest.objects.get(pk=follow_request_id)

            if follow_request.status == "accepted":
                return Response(
                    {"error": "You can not declined an accepted request"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except FollowRequest.DoesNotExist:
            return Response(
                {"error": "Follow request does not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = {"status": "declined"}
        serializer = FollowRequestSerializer(follow_request, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"], url_path="cancel-follow-request")
    def cancel_follow_request(self, request, *args, **kwargs):
        follow_request_id = kwargs.get("pk")

        try:
            follow_request = FollowRequest.objects.get(pk=follow_request_id)

            if follow_request.sender != request.user:
                return Response(
                    {"error": "You are not permitted to perform this action."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            elif follow_request.status != "not_accepted":
                return Response(
                    {
                        "error": f"Your request is already been responded as {follow_request.status}"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            else:
                follow_request.delete()
                return Response(
                    {"message": "Follow request cancelled successfully"},
                    status=status.HTTP_200_OK,
                )

        except FollowRequest.DoesNotExist:
            return Response(
                {"error": "Follow request does not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class FollowListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer

    def list(self, request, *args, **kwargs):
        user = request.user

        follower_queryset = Follow.objects.filter(following_id=user.id)
        follower_serializer = self.get_serializer(follower_queryset, many=True)

        following_queryset = Follow.objects.filter(follower_id=user.id)
        following_serializer = self.get_serializer(following_queryset, many=True)

        print("following:")
        print(following_serializer.data)
        print("follower:")
        print(follower_serializer.data)
        print(follower_queryset.count())

        response_data = {
            "follower_count": follower_queryset.count(),
            "follower_list": {
                "username": follower["follower"]["username"]
                for follower in follower_serializer.data
            },
            "following_count": following_queryset.count(),
            "following_list": {
                "username": following["following"]["username"]
                for following in following_serializer.data
            },
        }

        return Response(response_data)
