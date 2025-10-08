# PhysicsEquationSolver
Small application built in Python for allowing someone to calculate for unknown values using any of 5 different physics equations. This utilizes python math and streamlit. Both can be installed via pip inside the virtual environment.

## How to Install
**1. Make a New Python Virtual Environment**

```
python -m venv .venv
```

**2. Activate the virtual environment**

For more clarification on how to do this, I recommend looking at the [virtual environvment documentation.](https://docs.python.org/3/library/venv.html#how-venvs-work) 

**3. Use PIP to install Streamlit**

```
pip install streamlit 
```

**4. Use Streamlit to Run the App**

```
streamlit run frontend.py
```

## How to Use

After running the app, a new browser window should open using your default browser and you should immediately be presented with a webpage showing the basic velocity formula with two number inputs for either distance or time. Using the drop down menu, you can switch the selected equation to any of five different options including a secondary velocity formula, a vector velocity equation, a displacement formula and a kinetic energy formula.

## FAQ

1. Do I need to make a new virtual environment to run this project?

Unfortunately, I have not figured out a way to have streamlit to be able to run the project outside of the virtual environment so **you have to create the virtual environment in order to be able to use the browser**. 

2. Are you planning on keeping this project updated with more physics equations

Hopefully! I plan on adding a couple more formulas for varying topics but I'm trying not to add formulas which are just variations of the five that already exist. I am a little busy in my regular life so I don't know if I will update it frequently but I wanted to have a good selection of equations to start.