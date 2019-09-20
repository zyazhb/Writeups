Use dirbuster to fuzz dirs

found /api/

then fuzz file

found /api/action.php

then fuzz parameter

use /api/action.php?{dir}=dawa found /api/action.php?reset=dawa

finally fuzz id

found /api/action.php?reset=20 and the flag
