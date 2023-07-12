from django.shortcuts import render, redirect
from chat.models import Room,Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def room(request, room):
  username = request.GET.get('username')
  room_details=Room.objects.get(name=room)

  return render(request, 'room.html', {
    'username':username,
    'room':room,
    'room_details':room_details
  })

def checkview(request): #checks if the room was already created if not creates a new one
  room = request.POST['room_name']   #in home.html there is name='room_name' in input form
  username = request.POST['username'] #same here

  if Room.objects.filter(name=room).exists():
    return redirect('/'+room+'/?username='+username) #if room exits then redirect to it
  else:
    new_room = Room.objects.create(name=room) #if room doesnt exist then create it
    new_room.save()
    return redirect('/'+room+'/?username='+username)

def send(request):
  message = request.POST['message']
  username = request.POST['username']
  room_id = request.POST['room_id']

  new_message = Message.objects.create(value=message, user=username, room=room_id)
  new_message.save()
  return HttpResponse('Message sent sucessfully')

def getMessages(request, room):
  room_details = Room.objects.get(name=room) #accesing room model with the name == room
  messages = Message.objects.filter(room=room_details.id)

  return JsonResponse({"messages":list(messages.values())})