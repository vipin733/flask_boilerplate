class HomeController:

    #get dashboard home data
    def index(self):
        data = {
                "status": True,
                "message": "success",
                "user": {"name": "user" }
            }
        return data
          
       
