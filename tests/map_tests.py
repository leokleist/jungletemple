from nose.tools import *
from jungletemple.map import *




    
def ravine_test():
    assert_equal(ravine.paths.get("badswing"), death8)
    assert_equal(ravine.paths.get("badclimb"), death3)
    assert_equal(ravine.paths.get("badjump"), death2)
    assert_equal(ravine.paths.get("other"), death9)
    assert_equal(ravine.paths.get("goodswing"), skeletons)
    assert_equal(ravine.paths.get("goodclimb"), skeletons)
    assert_equal(ravine.paths.get("goodjump"), skeletons)
    
    
    
def test_two():  
    assert_equal(skeletons.go("sneak"), doors)
    assert_equal(skeletons.go("run"), death5 )
    assert_equal(doors.go("left"), treasure)
    assert_equal(treasure.go("chest"), death6)
    assert_equal(treasure.go("statue"), death7)
    assert_equal(doors.go("right"), death4)
    assert_equal(treasure.go("scoop"), victory )
    assert_equal(START.go("right"), death1)
    assert_equal(START.go("left"), ravine)
    