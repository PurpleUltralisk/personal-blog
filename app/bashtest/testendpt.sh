#!/bin/bash

indexres=$(curl -f -s 'http://localhost:5000' && echo "Test #1: Index page success" || echo "Test #1: Index page failed to load" )
indexres=$(echo $indexres | sed 's/^.*Test #/Test #/')
echo $indexres

healthres=$(curl -f -s 'http://localhost:5000/health' && echo "Test #2: Health page success" || echo "Test #2: Health page failed to load" )
healthres=$(echo $healthres | sed 's/^.*Test #/Test #/')
echo $healthres

healthres=$(curl -f -s 'http://localhost:5000/login' && echo "Test #3: Login page success" || echo "Test #3: Login page failed to load" )
healthres=$(echo $healthres | sed 's/^.*Test #/Test #/')
echo $healthres

healthres=$(curl -f -s -d "username=testing&password=testing" 'http://localhost:5000/login' && echo "Test #4: Login with user success" || echo "Test #4: Login with user failed" )
healthres=$(echo $healthres | sed 's/^.*Test #/Test #/')
echo $healthres

healthres=$(curl -f -s 'http://localhost:5000/register' && echo "Test #4: Register page success" || echo "Test #4: Register page failed to load" )
healthres=$(echo $healthres | sed 's/^.*Test #/Test #/')
echo $healthres