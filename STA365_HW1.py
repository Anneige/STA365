#!/usr/bin/env python
# coding: utf-8

# In[ ]:


STA365
Homework 1


# In[ ]:


Question 1
What proportion of students who answer this question quickly will pass the class? Assume the probability of passing the class is 0.9. Assume the probability of answering this question quickly is 0.6 if you'll pass the class, while the probability drops to 0.3 if you'll not pass the class.


# In[ ]:


Given information:
    Pr(pass) = 0.9
    Pr(quick|pass) = 0.6
    Pr(quick|fail) = 0.3


# In[ ]:


Pr(pass|quick) = Pr(pass)Pr(quick|pass) / Pr(quick)
    = Pr(pass)Pr(quick|pass) / (Pr(pass)Pr(quick|pass) + Pr(fail)Pr(quick|fail))
    = 0.94737


# In[ ]:


Question 2

