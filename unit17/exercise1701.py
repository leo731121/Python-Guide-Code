answer = "1234"
 
def ab_counter(answer, guess, ab):
   a = 0
   b = 0
   for i in guess:
      if i in answer:
         if guess.index(i) == answer.index(i):
            a += 1
         else:
            b += 1
 
   ab[0] = a
   ab[1] = b
 
if __name__ == "__main__":
   abcounter = [0, 0]
   times = 0
   while True:
      times += 1
      guess = input(": ")
      ab_counter(answer, guess, abcounter)
      if abcounter[0] == 4:
         print("Right!!")
         break
      else:
         print(str(abcounter[0]) + "A" + str(abcounter[1]) + "B")
 
   print("You guess " + str(times) + " times.")
  
# 檔名: exercise1701.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
