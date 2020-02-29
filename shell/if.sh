echo "You have provided the following arguments $arg1 $arg2 $arg3"
arg1="hello"
arg2="hello"
arg3="day"
if [ "$arg1" = "$arg2" -a "$arg1" != "$arg3" ]
then
    echo "Two of the provided args are equal."
    exit 3
elif [ "$arg1" = "$arg2" -a "$arg1" = "$arg3" ]
then
    echo "All of the specified args are equal"
    exit 0
else
    echo "All of the specified args are different"
    exit 4
fi
