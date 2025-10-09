# defining functions for use during my Physics class
# all code written by joegriffin2000
import math

PI = math.pi
G = 9.81

def velocity1(d:float=None,t:float=None,v:float=None,verbose:bool=False,packed_vals:list=None) -> float:
    """Solves for the velocity formula "v = d/t". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        d (float, optional): Distance. Defaults to None.
        t (float, optional): Time. Defaults to None.
        v (float, optional): Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "v"

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 3:
            d = packed_vals[0]
            t = packed_vals[1]
            v = packed_vals[2]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")

    try:
        d = float(d) if d is not None else None 
        t = float(t) if t is not None else None
        v = float(v) if v is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (d,t,v):({d},{t},{v})") if verbose else ValueError("Non Numerics Passed as Values") #if any values are not numeric
    
    if v is not None: 
        if d is None: #solving for d
            var = "d"
            result = v * t
        elif t is None: #solving for t
            var = "t"
            result = d/v
        else: 
            raise ValueError(f"No Unknowns Passed (d,t,v):({d},{t},{v})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else:
        if d is None or t is None:
            raise ValueError(f"Too Many Unknowns (d,t,v):({d},{t},{v})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = d/t #solving for v

    if verbose:
        print(f"velocity1: {var} = {result}")

    return result


def velocity2(vi:float=None,a:float=None,t:float=None,vf:float=None,verbose:bool=False,packed_vals:list=None)-> float:
    """Solves for the velocity formula "vf = vi + at". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        vi (float, optional): Initial Velocity. Defaults to None.
        a (float, optional): Acceleration. Defaults to None.
        t (float, optional): Time. Defaults to None.
        vf (float, optional): Final Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=None
    var = "vf" 

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 4: 
            vi = packed_vals[0]
            a = packed_vals[1]
            t = packed_vals[2]
            vf = packed_vals[3]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")

    try: 
        vi = float(vi) if vi is not None else None 
        a = float(a) if a is not None else None
        t = float(t) if t is not None else None
        vf = float(vf) if vf is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("Non Numerics Passed as Values")  #if any values are not numeric
    
    if vf is not None: 
        if vi is None: #solving for vi
            var = "vi"
            result = vf - (a * t)
        elif a is None: #solving for a
            var = "a"
            result = (vf - vi) / t
        elif t is None: #solving for t
            var = "t"
            result = (vf - vi) / a
        else: 
            raise ValueError(f"No Unknowns Passed (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else: 
        if vi is None or a is None or t is None:
            raise ValueError(f"Too Many Unknowns (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = vi + (a * t) #solving for vf
    
    if verbose:
        print(f"velocity2: {var} = {result}") 

    return result

def velocity_vector(i:float=None,j:float=None,r:float=None,verbose:bool=False,packed_vals:list=None)-> float:
    """Solves for the vector formula "vr^2 = vi^2 + vj^2". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        i (float, optional): Vector i Component. Defaults to None.
        j (float, optional): Vector j Component. Defaults to None.
        r (float, optional): Result Vector Magnitude. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "r"

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 3:
            i = packed_vals[0]
            j = packed_vals[1]
            r = packed_vals[2]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")

    try:
        i = float(i) if i is not None else None 
        j = float(j) if j is not None else None
        r = float(r) if r is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (i,j,r):({i},{j},{r})") if verbose else ValueError("Non Numerics Passed as Values") #if any values are not numeric
    
    if r is not None: 
        if i is None: #solving for i
            var = "i"
            result = math.sqrt(r**2 - j**2)
        elif j is None: #solving for j
            var = "j"
            result = math.sqrt(r**2 - i**2)
        else: 
            raise ValueError(f"No Unknowns Passed (i,j,r):({i},{j},{r})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else: 
        if j is None or i is None:
            raise ValueError(f"Too Many Unknowns (i,j,r):({i},{j},{r})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = math.sqrt(i**2 + j**2) #solving for r

    if verbose:
        print(f"velocity_vector: {var} = {result}")

    return result

def displacement(vi:float=None,t:float=None,a:float=None,x:float=None,verbose:bool=False,packed_vals:list=None)-> float:
    """Solves for the displacement formula "x = vi*t + 1/2*a*t^2". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        vi (float, optional): Initial Velocity. Defaults to None.
        t (float, optional): Time. Defaults to None.
        a (float, optional): Acceleration. Defaults to None.
        x (float, optional): Displacement. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "x"

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 4:
            vi = packed_vals[0]
            t = packed_vals[1]
            a = packed_vals[2]
            x = packed_vals[3]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")

    try:
        vi = float(vi) if vi is not None else None 
        t = float(t) if t is not None else None
        a = float(a) if a is not None else None
        x = float(x) if x is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("Non Numerics Passed as Values") #if any values are not numeric
    
    if x is not None: 
        if vi is None: #solving for vi
            var = "vi"
            result = (x - ((1/2)*a*(t**2)))/t
        elif t is None: #solving for t
            var = "t"
            result = math.sqrt((2 * (x - (vi * t))) / a)
        elif a is None: #solving for a
            var = "a"
            result = (2 * (x - (vi * t))) / (t**2)
        else: 
            raise ValueError(f"No Unknowns Passed (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else: 
        if vi is None or t is None or a is None:
            raise ValueError(f"Too Many Unknowns (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = (vi * t) + ((1/2)*a*(t**2)) #solving for x

    if verbose:
        print(f"displacement: {var} = {result}")

    return result

def kinetic_energy(m:float=None,v:float=None,ke:float=None,verbose:bool=False,packed_vals:list=None)-> float:
    """Solves for the kinetic energy formula "ke = 1/2*m*v^2". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        m (float, optional): Mass. Defaults to None.
        v (float, optional): Velocity. Defaults to None.
        ke (float, optional): Kinetic Energy. Defaults to None.
        verbose (bool, optional): Printing Result To STDOUT and Verbose Error Handling. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "ke"

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 3:
            m = packed_vals[0]
            v = packed_vals[1]
            ke = packed_vals[2]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")
    
    try:
        m = float(m) if m is not None else None 
        v = float(v) if v is not None else None
        ke = float(ke) if ke is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (m,v,ke):({m},{v},{ke})") if verbose else ValueError("Non Numerics Passed as Values") #if any values are not numeric
    
    if ke is not None: 
        if m is None: #solving for m
            var = "m"
            result = (ke * 2) / (v**2)
        elif v is None: #solving for v
            var = "v"
            result = math.sqrt((ke * 2) / m)
        else: 
            raise ValueError(f"No Unknowns Passed (m,v,ke):({m},{v},{ke})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else: 
        if m is None or v is None: 
            raise ValueError(f"Too Many Unknowns (m,v,ke):({m},{v},{ke})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = m * (v**2) * 0.5 #solving for ke

    if verbose:
        print(f"kinetic_energy: {var} = {result}")

    return result

def potential_energy(m:float=None,h:float=None,pe:float=None,verbose:bool=False,packed_vals:list=None)-> float:
    """Solves for the kinetic energy formula "pe = m*g*h". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        m (float, optional): Mass. Defaults to None.
        h (float, optional): Height. Defaults to None.
        ke (float, optional): Potential Energy. Defaults to None.
        verbose (bool, optional): Printing Result To STDOUT and Verbose Error Handling. Defaults to False.
        packed_vals (list, optional): All values passed through a list instead of individually. Defaults to None.

    Raises:
        ValueError: Values passed through the packed list must be in the correct format
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "pe"

    #utilizing packed values. will be trumped by values passed individually.
    if packed_vals is not None:
        if isinstance(packed_vals,list) and len(packed_vals) == 3:
            m = packed_vals[0]
            h = packed_vals[1]
            pe = packed_vals[2]
        else:
            raise ValueError(f"Values Passed through Packed List in Wrong Format")
    
    try:
        m = float(m) if m is not None else None 
        h = float(h) if h is not None else None
        pe = float(pe) if pe is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (m,h,pe):({m},{h},{pe})") if verbose else ValueError("Non Numerics Passed as Values") #if any values are not numeric
    
    if pe is not None: 
        if m is None: #solving for m
            var = "m"
            result = pe / (G * h)
        elif h is None: #solving for h
            var = "h"
            result = pe / (G * m)
        else:  
            raise ValueError(f"No Unknowns Passed (m,h,pe):({m},{h},{pe})") if verbose else ValueError("No Unknowns Passed") #if all values are provided
    else: 
        if m is None or h is None: 
            raise ValueError(f"Too Many Unknowns (m,h,pe):({m},{h},{pe})") if verbose else ValueError("Too Many Unknowns") #if more than one value is unknown
        
        result = m * G * h #solving for pe

    if verbose:
        print(f"potential_energy: {var} = {result}")

    return result

if __name__ == "__main__":
    potential_energy(
        m=20,
        h=4,
        verbose=True
        )