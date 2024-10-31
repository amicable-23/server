from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework import serializers
from .models import user
from rest_framework.permissions  import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

# Create your views here.
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
        
    def create(self,data):
        newuser = user.objects.create_user(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password'],
            image = data['image'],
        )
        return newuser

class Signup(CreateAPIView):
    queryset = user.objects.all()
    serializer_class = userserializer
    
class Userview(RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = userserializer
    permission_classes = [ IsAuthenticated ]
    
    
class fetchuser(GenericAPIView):
    permission_classes =[ IsAuthenticated]
    serializer_class = userserializer
    
    def get(self, request):
        print(request.user.id)
        
        User = user.objects.get(id = request.user.id)
        serializers = self.serializer_class(User)
        
        return Response(data = serializers.data, status=200)
    
