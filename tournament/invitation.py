import cts.application.row

#use 'accepted' flag instead of function calls?
class invitation(cts.application.row.row):
    def __init__(self, inviter, invitee, accept_func, decline_func):
        """accept_func and decline_func take 1 parameter each, the object accepting/declining"""
        self.inviter = inviter
        self.invitee = invitee
        self.accept_func = accept_func
        self.decline_func = decline_func
        cts.application.row.row.__init__(self, dict(inviter=self.inviter.GetName(), invitee=self.invitee.GetName()))
    
    def GetInviter(self):
        return self.inviter
        
    def GetInvitee(self):
        return self.invitee
        
    def Accept(self):
        return self.accept_func(self.invitee)
        
    def Decline(self):
        self.decline_func(self)