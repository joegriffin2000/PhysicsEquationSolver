import equations as eq
import streamlit as st

#this needs to map the equations script functions. ANY errors here will screw everything else up
mappings = {
    "names":["Velocity 1","Velocity 2","Velocity Vector","Displacement","Kinetic Energy"],
    "functions":[eq.velocity1,eq.velocity2,eq.velocity_vector,eq.displacement,eq.kinetic_energy],
    "formulas":[
        r'''v = \left(\frac{d}{t}\right)''',
        r'''v_f = v_i + a*t''',
        r'''v*r^2 = v*i^2 + v*j^2''',
        r'''x = v_i*t + \frac 1 2*a*t^2''',
        r'''KE = \frac 1 2*m*v^2'''],
    "parameters":[
        ("d","t","v"),
        ("vi","a","t","vf"),
        ("i","j","r"),
        ("vi","t","a","x"),
        ("m","v","ke"),
        ]
    }

def parameter_unpacker(func:callable,values:list):
    try:
        return func(packed_vals=values)
    except TypeError:
        return None
    except ValueError:
        return None


st.title("Physics Formula Solver")
st.write("Select the Formula You Would Like to Use")

col1, col2 = st.columns([8,2])

option = col1.selectbox(
    "equation_select",
    options=mappings["names"],
    label_visibility="collapsed"
    )

index = mappings["names"].index(option)

excludeLast = col2.toggle(f"Exclude {mappings["parameters"][index][-1].upper()}",value=True)

st.latex(mappings["formulas"][index])

st.divider()

parameters = mappings["parameters"][index]
parameter_columns = st.columns(len(parameters),gap=None,border=True) if not excludeLast else st.columns(len(parameters)-1,gap=None,border=True)

param_vals = [None]*len(parameters)

for i in range(len(parameter_columns)):
    with parameter_columns[i]:
        head,val = st.columns([7,8],gap=None,vertical_alignment="bottom")
        head.subheader(parameters[i] + " = ", width="content")
        temp = val.number_input(
            parameters[i],
            value=None,
            step=None,
            format="%0.4f",
            label_visibility="collapsed")
        param_vals[i] = temp

res = parameter_unpacker(mappings["functions"][index],param_vals)

if res is not None:
    with st.container(border=True):
        st.title("Result:")
        st.header(res)
