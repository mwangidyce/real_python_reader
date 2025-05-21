PROJECT="visits"


if [[ ${PROJECT} == "common" ]]; then
    workdir="./common"
elif test -d "./services/${PROJECT}"; then
    workdir="./services/${PROJECT}"
elif test -d "./tools/${PROJECT}"; then
    workdir="./tools/${PROJECT}"
fi





echo ${workdir}