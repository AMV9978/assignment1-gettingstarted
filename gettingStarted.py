### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "The student should type the answer here"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "The student should type the answer here"
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    answer = "pcap"
#"Are encoding and encryption the same? - Yes/No":
if question == "Are encoding and encryption the same? - Yes/No":
    answer = "No"
    
#"Is it possible to decrypt a message without a key? - Yes/No":
if question == "Is it possible to decrypt a message without a key? - Yes/No":
   answer = "No"
    
#"Is it possible to decode a message without a key? - Yes/No":
 if question == "Is it possible to decode a message without a key? - Yes/No":  
     answer = "Yes"
     
#"Is a hashed message supposed to be un-hashed? - Yes/No":
 if quesiton == "Is a hashed message supposed to be un-hashed? - Yes/No":
    answer = "No" 

#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
 if question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
     answer = "1f2ed969e2a8c807039d9cf76c7b3f6defbe3ec064339f39a9f2ac372aac4dcd"
    
#"Is MD5 a secured hashing algorithm? - Yes/No":
  if question == "Is MD5 a secured hashing algorithm? - Yes/No":
      answer = "No"
    
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
 if question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
    answer = "4"

#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
 if question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
    answer = "2"

