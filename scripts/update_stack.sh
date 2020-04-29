echo "Update stack ..."
aws cloudformation update-stack \
--stack-name covid-dash \
--template-body "$(cat stacks/aws-cluster.yml)" \
--parameters "$(cat stacks/aws-cluster.json)" \
--capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" \
--region=us-west-2