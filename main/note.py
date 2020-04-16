   #orders = Order.objects.all()
    #response_data = {}
#
 #   if request.POST.get('action') == 'post':
  #      client_name = request.POST.get('client_name')
   #     phone = request.POST.get('phone')
    #    device_type = request.POST.get('device_type')
     #   brand = request.POST.get('brand')
      #  model = request.POST.get('model')
#
 #       response_data['client_name'] = client_name
  #      response_data['phone'] = phone
   #     response_data['device_type'] = device_type
    #    response_data['brand'] = brand
     #   response_data['model'] = model
#
 #       Post.objects.create(
  #          client_name = client_name,
   #         phone = phone,
    #        device_type = device_type,
     #       brand = brand,
      #      model = model,
       # )
        #
        #return JsonResponse(response_data)
    #return render(request, 'main/index.html', {'orders': orders})