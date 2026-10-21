# 1. Fork this repo

1. On this GitHub repo, look for the **Fork** button on the upper right. 

<img src="assets/fork.png" width="500">

2. Click `create a new fork` and follow the instructions. 


# 2. Clone the fork locally

On your forked GitHub repository page (make sure it is the repo on your account), click the green **Code** button and copy the clone URL (HTTPS). 

In your local terminal, navigate to where you store projects, create a new folder and clone your repository:

```sh
ls 
cd python-projects # where you store all your python folders
mkdir github-practice # create the new folder for this repo
cd github-practice
git clone your-copied-fork-url
code .
```


If your main branch doesn't exist, create it:
```sh
git switch -c main
```

# 3. Create and activate your environment. This will be different depending on which IDE (jupyer notebook vs VS Code) you're in. 

1. Jupyter Notebook:

Create your environment by clicking on the kernel in the top right corner of the notebook and selecting .venv or run the following code:

MacOS/Linux
```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ipykernel
python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
```

Windows Command Prompt
```sh
python -m venv .venv
.venv\Scripts\activate
python -m pip install ipykernel
python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
```

Windows Power Shell
```sh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install ipykernel
python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
```


2. VS Code: 

Create your environment and activate it:
MacOS/Linux
```sh
python3 -m venv .venv
source .venv/bin/activate
```
Windows Command Prompt
```sh
python -m venv .venv
.venv\Scripts\activate
```

Windows PowerShell
```sh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If your environment in python does not work, you may need to reset your environment by turning it off and on and then reinstalling your imported libraries.
```sh
deactivate
```


# 4. Install pandas library to your environment.
```sh
python -m pip install --upgrade pip # may be unnecessary if you have already done this installation
python -m pip install pandas
```


# 5. In your local application, find and fix the errors in `analysis.py`.

1. Run the code:
```sh
python filename.py #e.g. python exercise_one.py
```
2. Fix the paths and information that is left blank in the `#TODO` section.

3. Read the code and find the syntax and spelling errors in the code. 

If it runs but doesn't print anything, that's a bug too. 

The program should print something like this depending on the column you choose:
```sh
Rows: 50
Mean: 428.68999999999994
Max: 936.7
Min: 169.7
```

# 6. After the app runs successfully, commit and push your changes to your repo. 

```sh
git add analysis.py
git commit -m "Fix errors in analysis.py"
git push origin branch-name # branch name will be main unless you made a separate branch
```

Make sure you push from the correct branch, whether you've made changes on your main branch or another branch.


# 7. Look at your changes on your repo. 

You may need to do a pull request first if you created a branch.
