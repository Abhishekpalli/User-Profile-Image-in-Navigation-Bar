class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self,request):
        form = ProfileForm()
        return render (request, self.template_name, {'form':form})

    def post(self, request):
         if request.method == 'POST':
         	form_old = ProfileForm(data=request.POST, files=request.FILES)
            if form_old.is_valid() and 'image' in request.FILES:
            	    request.user.userprofile.image.delete()

            form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                  form.save()
        else:
            form = ProfileForm(instance=request.user.userprofile)
        return render (request, self.template_name, {'form':form})
