#!/bin/sh

out_dir=atrax_keeper/output
mkdir -p ${out_dir}

tar -cvf ${out_dir}/atrax_keeper.tar --exclude=*.pyc --exclude=deployment --exclude=output --exclude=.idea* \
../../python_common \
../../atrax/management ../../atrax/common ../../atrax/fetcher ../../atrax/frontier ../../atrax/__init__.py \
../../atrax/prior_versions atrax/deployment/*.jinja2 atrax/deployment/cloud_config.txt \
../../aws/*.py ../../aws/ec2 ../../aws/s3 ../../aws/sdb ../../aws/sns ../../aws/sqs \
atrax_keeper

# Add run.sh to the top level of the tar file
current_dir=`pwd`
cd atrax_keeper/deployment
tar -rvf ${current_dir}/${out_dir}/atrax_keeper.tar run.sh
cd ${current_dir}

cp atrax_keeper/deployment/debian_env_setup.sh ${out_dir}/
