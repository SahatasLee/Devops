#! /usr/bin/bash
main () {
    # your main function code here   
    name=${1:-"you"}
    echo "One for $name, one for me."
}

# call main with all of the positional arguments
main "$@"