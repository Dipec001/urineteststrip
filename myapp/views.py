from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from .imageprocessor import process_image
from .models import UploadedImage
from .serializers import UploadedImageSerializer


from django.shortcuts import render

class ColorIdentificationView(APIView):
    def post(self, request):
        try:
            # Get the uploaded image from the request
            uploaded_image = request.FILES.get('image')

            if not uploaded_image:
                return Response({'error': 'No image file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the image to the media folder
            fs = FileSystemStorage(location='media/')
            filename = fs.save(uploaded_image.name, uploaded_image)

            # Create an instance of your UploadedImage model
            uploaded_image_instance = UploadedImage(image=filename)
            uploaded_image_instance.save()

            # Call the process_image function to identify colors
            identified_colors = process_image(filename)
            print(filename)

            # Return the identified colors in the response
            return Response(identified_colors, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        




def index(request):
    return render(request, 'index.html')

