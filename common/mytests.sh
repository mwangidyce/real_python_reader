PROJECT="visits"


for file in SQL/*.sql; do
    mysql -h 127.0.0.1 -u root -ppassword integrations_db < ${file}
done




echo ${workdir}