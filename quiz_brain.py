class quizbrain :
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score= 0


    def ques_ask(self):
        curren_ques = self.question_list[self.question_no]
        self.question_no +=1
        user_ans = input(f"Q.{self.question_no}: {curren_ques.text} (True/False): ")
        self.check_ans(user_ans,curren_ques.answer)



    def still_has_ques(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def check_ans(self,user_ans,cor_ans):
        if user_ans.lower()==cor_ans.lower():
            self.score +=1
            print("You got it right!")
            print(f"Current score {self.score}/{self.question_no}")
        else:
            print("That's wrong.")
            print(f"Current score {self.score}/{self.question_no}")
        print(f"The Correct answer was: {cor_ans}")