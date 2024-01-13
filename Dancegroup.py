class GetcountException(Exception):
    pass


class DanceGroup:
    def __init__(self, Count, groupname):
        # self.leader = leader
        self.groupname = groupname
        self.GroupCount = Count
        print(
            f"\nDance Group '{self.groupname}' created.\nGroup Count = {self.GroupCount}")

    def Get_count(self):
        print(
            f"\nDance Group '{self.groupname}' \nGroup count = {self.GroupCount}")

    def Performer(self, member):
        self.GroupCount = self.GroupCount + member

        print(
            "\nPerformer for Annual Day added....")
        self.Get_count()

    def disqualify(self, member):
        if self.GroupCount >= member:
            return
        else:
            raise GetcountException(
                f"\nSorry, You are Disqualify '{self.groupname}' \n{self.GroupCount}"
            )

    def Notperforming(self, member, ):
        try:
            self.disqualify(member)
            self.GroupCount = self.GroupCount - member
            print("\nMember removed from not performing list.")
            # self.GroupCount()
        except GetcountException as error:
            print(f'\nPerformer interrupted:{error}')

    def Anotherperformer(self, member):
        try:
            print("\n************\n\nBeginning Anotherperformer*****************")
            self.disqualify(member)
            self.Notperforming(member)
            # newmember.performing(member)
            print('\nPerofrmed Complete!💃💃\n\n********')
        except GetcountException as error:
            print(f'\nPerform Interrupted. 🤾‍♂️🤾‍♀️{error}')


class Winnerrewardsdance(DanceGroup):
    def Performer(self, member):
        self.GroupCount = self.GroupCount + (member * 1)
        print('\nDance Reward completed.')
        self.Get_count()


class Winner(Winnerrewardsdance):
    def __init__(self, groupname, GroupCount):
        super().__init__(groupname, GroupCount)
        self.win = 2

    def Performer(self, member):
        try:
            self.Notperforming(member + self.win)
            self.GroupCount = self.GroupCount - (member + self.win)
            print('\nWinner!!!')
            self.Get_count()
        except GetcountException as error:
            print(f'\nPerformance Interrupted. 🏆🎉{error}\n')
