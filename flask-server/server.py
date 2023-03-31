from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request
import pandas as pd
import os
from supabase import create_client, Client

app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#Members API Route
@app.route("/projects")
def get_all_projects():
    response = supabase.table('projects').select("*").execute()
    # print(response)
    # df = pd.read_csv('projects_db.csv')
    # results = df.to_dict("records")
    results = response.data
    return results

@app.route("/issues")
def get_all_issues():
    response = supabase.table('issues').select("*").execute()
    results = response.data
    return results

@app.route("/actions")
def get_all_actions():
    response = supabase.table('actions').select("*").execute()
    return response.data

@app.route("/risks")
def get_all_risks():
    response = supabase.table('risks').select("*").execute()
    return response.data

@app.route("/project", methods = ['GET', 'POST', 'DELETE'])
def project():
    if request.method == 'GET':
        args = request.args
        response = supabase.table('projects').select("*").eq('id', args.get("project_id")).execute()
        return response


    if request.method == 'POST':
        # changes
        print('/project POST Request')
        print(request.json)
        proj = request.json
        data = supabase.table("projects").insert({"name":proj["name"],"description":proj["description"],"budget":proj["budget"]}).execute()
        # data = request.json
        print('supabase response')
        print(data.data)
        return data.data

    if request.method == 'DELETE':
        args = request.args
        data = supabase.table("projects").delete().eq("id", args.get("project_id")).execute()

    else:
        print("Error 405 Method Not Allowed")



    
@app.route("/action", methods = ['GET', 'POST', 'DELETE'])
def action():
    if request.method == 'GET':
        args = request.args
        response = supabase.table('actions').select("*").eq('id', args.get("action_id")).execute()
        return response.data


    if request.method == 'POST':
        # changes
        print('/action POST Request')
        print(request.json)
        obj = request.json
        data = supabase.table("actions").insert({"name":obj["name"],"description":obj["description"],"status":obj["status"],"project_id":obj["project_id"]}).execute()
        print('supabase response')
        print(data.data)
        return data.data

    if request.method == 'DELETE':
        args = request.args
        data = supabase.table("actions").delete().eq("id", args.get("action_id")).execute()

    else:
        print("Error 405 Method Not Allowed")


@app.route("/issue", methods = ['GET', 'POST', 'DELETE'])
def issue():
    if request.method == 'GET':
        args = request.args
        response = supabase.table('issues').select("*").eq('id', args.get("issue_id")).execute()
        return response.data


    if request.method == 'POST':
        # changes
        print('/issue POST Request')
        print(request.json)
        obj = request.json
        data = supabase.table("issues").insert({"name":obj["name"],"description":obj["description"],"status":obj["status"],"project_id":obj["project_id"]}).execute()
        print('supabase response')
        print(data.data)
        return data.data

    if request.method == 'DELETE':
        args = request.args
        data = supabase.table("issues").delete().eq("id", args.get("issue_id")).execute()

    else:
        print("Error 405 Method Not Allowed")


@app.route("/risk", methods = ['GET', 'POST', 'DELETE'])
def risk():
    if request.method == 'GET':
        args = request.args
        response = supabase.table('risks').select("*").eq('id', args.get("risk_id")).execute()
        return response.data


    if request.method == 'POST':
        # changes
        print('/risk POST Request')
        print(request.json)
        obj = request.json
        data = supabase.table("risks").insert({"name":obj["name"],"description":obj["description"],"status":obj["status"],"project_id":obj["project_id"]}).execute()
        print('supabase response')
        print(data.data)
        return data.data

    if request.method == 'DELETE':
        args = request.args
        data = supabase.table("risks").delete().eq("id", args.get("risk_id")).execute()

    else:
        print("Error 405 Method Not Allowed")


    
if __name__ == "__main__":
    app.run(debug=True)