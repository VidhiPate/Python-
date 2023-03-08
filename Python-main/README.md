Steps To connect FASTAPI with Oracle Database:
 1) install cx_oracle by using pip install cx_Oracle.
 2) install FAST API by using pip install fastapi and uvicorn server by using pip install uvicorn.
 3) Then create a files same as main.py and orcl.py and change the credentials in main.py.
 4) And after that Start the uvicorn server by using this command "uvicorn main:app --reload"
 5) You will some output in your shell or cmd
 6) ![image](https://user-images.githubusercontent.com/55869588/213310218-30ae78c5-8ba6-489e-b3d9-fea93d99958d.png)
open that url and 
![image](https://user-images.githubusercontent.com/55869588/213310331-63e38c5d-60a0-48eb-9425-f5cef2bf1ee3.png)
change or add the value /"your  table name" in my case it was /emp.
You will see I got my data
![image](https://user-images.githubusercontent.com/55869588/213310449-cc50d74b-667a-4915-9abb-1d00ad60eba5.png)
