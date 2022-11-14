from multiprocessing import context
from django.shortcuts import render, redirect
from .models import QueryHolder, HelperModel
import json
import requests

url = 'https://qtest.eng.netapp.com'
projectId = 67


def new_home(request):
    if request.method == 'POST':
        type_new_modify = request.POST.get('type_new_modify')
        report_name = request.POST.get('report_name')
        if type_new_modify == 'new':
            return render(request, 'burt/home.html')
        else:
            pass
    else:
        return render(request, 'burt/new_home.html')

def QTestHandler(query):
    # token = ''

    # payload='grant_type=password&username=cse_automation@netapp.com&password=NetApp1!'
    # headers1 = {
    # 'Authorization': 'Basic Y3NlX2F1dG9tYXRpb25AbmV0YXBwLmNvbTo=',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'qtest-8080=s15'
    # }
    # r = requests.request('POST', f'{url}/oauth/token', data=payload, headers=headers1)
    # token = r.json()['access_token']

    # headers2 = {
    #     'Authorization': f'bearer {token}',
    #     'Content-Type': 'application/json'
    # }
    # data = {
    # "object_type": "test-runs",
    # "fields": ["*"],
    # "query": query
    # } 

    # r = requests.request('POST', f'{url}/api/v3/projects/{projectId}/search', headers=headers2, data=json.dumps(data))
    # print(r.json())

    data123 = {'items': [
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "Yes",
         "testCaseId": 524837,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524837?versionId=827207&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247386"
            }
         ],
         "id": 247386,
         "name": "PVT_NIC_RSSv4_Singlemode_Ifgrp",
         "order": 1,
         "pid": "TR-5",
         "created_date": "2017-12-11T06:48:30+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "1"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524837,
            "test_case_version_id": 827207,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44162,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827207,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524838,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524838?versionId=827208&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247387"
            }
         ],
         "id": 247387,
         "name": "PVT_NIC_RSSv4_Multimode_Ifgrp",
         "order": 2,
         "pid": "TR-6",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "2"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524838,
            "test_case_version_id": 827208,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44163,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827208,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524839,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524839?versionId=827209&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247388"
            }
         ],
         "id": 247388,
         "name": "PVT_NIC_RSSv4_Multimode_LACP_Ifgrp",
         "order": 3,
         "pid": "TR-7",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "3"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524839,
            "test_case_version_id": 827209,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44164,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827209,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524843,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524843?versionId=827212&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247389"
            }
         ],
         "id": 247389,
         "name": "PVT_NIC_RSSv4_VLAN",
         "order": 4,
         "pid": "TR-8",
         "created_date": "2017-12-14T09:30:02+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "4"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120450"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524843,
            "test_case_version_id": 827212,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44226,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 827212,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524844,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524844?versionId=827213&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247390"
            }
         ],
         "id": 247390,
         "name": "PVT_NIC_RSSv4_Multimode_LACP_Ifgrp_VLAN",
         "order": 5,
         "pid": "TR-9",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "5"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524844,
            "test_case_version_id": 827213,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44165,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827213,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524848,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524848?versionId=827214&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247391"
            }
         ],
         "id": 247391,
         "name": "PVT_NIC_RSSv4_ICMP_MTU_1500",
         "order": 6,
         "pid": "TR-10",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "6"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524848,
            "test_case_version_id": 827214,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44166,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827214,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524849,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524849?versionId=827215&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247392"
            }
         ],
         "id": 247392,
         "name": "PVT_NIC_RSSv4_ICMP_MTU_9000",
         "order": 7,
         "pid": "TR-11",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "7"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524849,
            "test_case_version_id": 827215,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44167,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827215,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542687,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542687?versionId=834047&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247393"
            }
         ],
         "id": 247393,
         "name": "PVT_NIC_RSSV4_VLAN_MTU",
         "order": 8,
         "pid": "TR-12",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "8"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542687,
            "test_case_version_id": 834047,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44168,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834047,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524907,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524907?versionId=827240&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247394"
            }
         ],
         "id": 247394,
         "name": "PVT_NIC_LROV4_MTU",
         "order": 9,
         "pid": "TR-13",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "9"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524907,
            "test_case_version_id": 827240,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44169,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827240,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524908,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524908?versionId=827241&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247395"
            }
         ],
         "id": 247395,
         "name": "PVT_NIC_LROV4_VLAN",
         "order": 10,
         "pid": "TR-14",
         "created_date": "2017-12-14T09:24:34+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "10"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524908,
            "test_case_version_id": 827241,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44170,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827241,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524909,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524909?versionId=827242&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247396"
            }
         ],
         "id": 247396,
         "name": "PVT_NIC_LROV4_Multimode_LACP_Ifgrp_VLAN",
         "order": 11,
         "pid": "TR-15",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "11"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524909,
            "test_case_version_id": 827242,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44171,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827242,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542654,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542654?versionId=834038&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247397"
            }
         ],
         "id": 247397,
         "name": "PVT_NIC_LROv4_Link_Toggle_test",
         "order": 12,
         "pid": "TR-16",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "12"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542654,
            "test_case_version_id": 834038,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44172,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834038,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542657,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542657?versionId=834039&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247398"
            }
         ],
         "id": 247398,
         "name": "PVT_NIC_LROV4_VLAN_MTU",
         "order": 13,
         "pid": "TR-17",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "13"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542657,
            "test_case_version_id": 834039,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44173,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834039,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524859,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524859?versionId=827223&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247399"
            }
         ],
         "id": 247399,
         "name": "PVT_NIC_TSO6_IFSTAT_NETSTAT_OFF_ON_NFS",
         "order": 14,
         "pid": "TR-18",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "14"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524859,
            "test_case_version_id": 827223,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44174,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827223,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524860,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524860?versionId=827224&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247400"
            }
         ],
         "id": 247400,
         "name": "PVT_NIC_TSO6_MTU",
         "order": 15,
         "pid": "TR-19",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "15"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524860,
            "test_case_version_id": 827224,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44175,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827224,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524861,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524861?versionId=827225&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247401"
            }
         ],
         "id": 247401,
         "name": "PVT_NIC_TSO6_MTU9000_RWSIZE32K",
         "order": 16,
         "pid": "TR-20",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "16"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524861,
            "test_case_version_id": 827225,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44176,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827225,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524866,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524866?versionId=689292&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247402"
            }
         ],
         "id": 247402,
         "name": "PVT_NIC_TSO6_Multimode_LACP_Ifgrp",
         "order": 17,
         "pid": "TR-21",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "17"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524866,
            "test_case_version_id": 689292,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44177,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 689292,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524870,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524870?versionId=827231&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247403"
            }
         ],
         "id": 247403,
         "name": "PVT_NIC_TSO6_Multimode_LACP_Ifgrp_VLAN",
         "order": 18,
         "pid": "TR-22",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "18"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524870,
            "test_case_version_id": 827231,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44178,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 827231,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542632,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542632?versionId=734204&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247404"
            }
         ],
         "id": 247404,
         "name": "PVT_NIC_TSO6_ifgrp_singlemode",
         "order": 19,
         "pid": "TR-23",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "19"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542632,
            "test_case_version_id": 734204,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44179,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734204,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542648,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542648?versionId=734124&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247405"
            }
         ],
         "id": 247405,
         "name": "PVT_NIC_TSO6_VLAN",
         "order": 20,
         "pid": "TR-24",
         "created_date": "2017-12-14T09:24:35+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "20"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542648,
            "test_case_version_id": 734124,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44180,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734124,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 525508,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/525508?versionId=827721&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247406"
            }
         ],
         "id": 247406,
         "name": "PVT_NIC_LMF_v6_Multicast_large_aliases",
         "order": 21,
         "pid": "TR-25",
         "created_date": "2017-12-14T09:30:57+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "21"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120845"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 525508,
            "test_case_version_id": 827721,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44227,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 827721,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 526566,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/526566?versionId=828497&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247407"
            }
         ],
         "id": 247407,
         "name": "PVT_NIC_OFFLOAD_NET_OPT_MODIFY_IPV6_TRUE",
         "order": 22,
         "pid": "TR-26",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "22"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 526566,
            "test_case_version_id": 828497,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44181,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 828497,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 526568,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/526568?versionId=828499&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247408"
            }
         ],
         "id": 247408,
         "name": "PVT_NIC_OFFLOAD_NET_INT_CREATE_MODIFY",
         "order": 23,
         "pid": "TR-27",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "23"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 526568,
            "test_case_version_id": 828499,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44182,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 828499,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 526578,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/526578?versionId=828507&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247409"
            }
         ],
         "id": 247409,
         "name": "PVT_NIC_OFFLOAD_IFGRP_NFS_READ_IPv6_NFS_WRITE_IPv4",
         "order": 24,
         "pid": "TR-28",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "24"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 526578,
            "test_case_version_id": 828507,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44183,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 828507,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 527065,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/527065?versionId=707674&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247410"
            }
         ],
         "id": 247410,
         "name": "PVT_NIC_Spirent_CRC_Errors",
         "order": 25,
         "pid": "TR-29",
         "created_date": "2017-12-14T09:31:20+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "25"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120751"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 527065,
            "test_case_version_id": 707674,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44228,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 707674,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 527066,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/527066?versionId=707523&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247411"
            }
         ],
         "id": 247411,
         "name": "PVT_NIC_Spirent_Runt_Errors",
         "order": 26,
         "pid": "TR-30",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "26"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 527066,
            "test_case_version_id": 707523,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44184,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 707523,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 527067,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/527067?versionId=707694&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247412"
            }
         ],
         "id": 247412,
         "name": "PVT_NIC_Spirent_Long_Frames",
         "order": 27,
         "pid": "TR-31",
         "created_date": "2017-12-14T09:31:45+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "27"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120758"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 527067,
            "test_case_version_id": 707694,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44229,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 707694,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 527069,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/527069?versionId=707738&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247413"
            }
         ],
         "id": 247413,
         "name": "PVT_NIC_Spirent_Jabber",
         "order": 28,
         "pid": "TR-32",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "28"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 527069,
            "test_case_version_id": 707738,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44185,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 707738,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540748,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540748?versionId=733198&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247414"
            }
         ],
         "id": 247414,
         "name": "PVT_NIC_Spirent Unicast 64B Frame",
         "order": 29,
         "pid": "TR-33",
         "created_date": "2017-12-14T09:24:36+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "29"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540748,
            "test_case_version_id": 733198,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44186,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733198,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540749,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540749?versionId=733098&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247415"
            }
         ],
         "id": 247415,
         "name": "PVT_NIC_Spirent Multicast 64B Frame",
         "order": 30,
         "pid": "TR-34",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "30"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540749,
            "test_case_version_id": 733098,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44187,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733098,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540750,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540750?versionId=733199&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247416"
            }
         ],
         "id": 247416,
         "name": "PVT_NIC_Spirent Broadcast 64B Frame",
         "order": 31,
         "pid": "TR-35",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "31"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540750,
            "test_case_version_id": 733199,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44188,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733199,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540766,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540766?versionId=733206&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247417"
            }
         ],
         "id": 247417,
         "name": "PVT_NIC_Spirent_V4_TCP_Port_2049",
         "order": 32,
         "pid": "TR-36",
         "created_date": "2017-12-14T09:32:07+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "32"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120431 "
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540766,
            "test_case_version_id": 733206,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44230,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 733206,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540790,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540790?versionId=733260&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247418"
            }
         ],
         "id": 247418,
         "name": "PVT_NIC_Spirent_ICMP traffic",
         "order": 33,
         "pid": "TR-37",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "33"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540790,
            "test_case_version_id": 733260,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44189,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733260,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540791,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540791?versionId=733226&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247419"
            }
         ],
         "id": 247419,
         "name": "PVT_NIC_Spirent_ICMP6 traffic",
         "order": 34,
         "pid": "TR-38",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "34"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540791,
            "test_case_version_id": 733226,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44190,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733226,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542386,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542386?versionId=733980&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247420"
            }
         ],
         "id": 247420,
         "name": "PVT_NIC_Spirent_Frag_Frames",
         "order": 35,
         "pid": "TR-39",
         "created_date": "2017-12-14T09:32:24+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "35"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120762"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542386,
            "test_case_version_id": 733980,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44231,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 733980,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542387,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542387?versionId=733989&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247421"
            }
         ],
         "id": 247421,
         "name": "PVT_NIC_Spirent_Jumbo",
         "order": 36,
         "pid": "TR-40",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "36"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542387,
            "test_case_version_id": 733989,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44191,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733989,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 534029,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/534029?versionId=729230&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247422"
            }
         ],
         "id": 247422,
         "name": "PVT_NIC_Sysconfig_Device_FW_Check",
         "order": 37,
         "pid": "TR-41",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "37"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 534029,
            "test_case_version_id": 729230,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44192,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 729230,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 534030,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/534030?versionId=729193&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247423"
            }
         ],
         "id": 247423,
         "name": "PVT_NIC_Sysconfig_SN_check",
         "order": 38,
         "pid": "TR-42",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "38"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 534030,
            "test_case_version_id": 729193,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44193,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 729193,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542425,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542425?versionId=733920&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247424"
            }
         ],
         "id": 247424,
         "name": "PVT_NIC_sysconfig_M",
         "order": 39,
         "pid": "TR-43",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "39"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542425,
            "test_case_version_id": 733920,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44194,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 733920,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542627,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542627?versionId=734174&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247425"
            }
         ],
         "id": 247425,
         "name": "PVT_NIC_Sysconfig_network_port_show",
         "order": 40,
         "pid": "TR-44",
         "created_date": "2017-12-14T09:34:05+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "40"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120139"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542627,
            "test_case_version_id": 734174,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44232,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 734174,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530337,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530337?versionId=829856&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247426"
            }
         ],
         "id": 247426,
         "name": "PVT_NIC_RSSV6_SINGLE_MODE_IFGRP",
         "order": 41,
         "pid": "TR-45",
         "created_date": "2017-12-14T09:24:37+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "41"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530337,
            "test_case_version_id": 829856,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44195,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829856,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530338,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530338?versionId=829857&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247427"
            }
         ],
         "id": 247427,
         "name": "PVT_NIC_RSSV6_MULTIMODE_IFGRP",
         "order": 42,
         "pid": "TR-46",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "42"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530338,
            "test_case_version_id": 829857,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44196,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829857,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530339,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530339?versionId=829858&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247428"
            }
         ],
         "id": 247428,
         "name": "PVT_NIC_RSSV6_MULTIMODE_LACP_IFGRP",
         "order": 43,
         "pid": "TR-47",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "43"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530339,
            "test_case_version_id": 829858,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44197,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829858,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530340,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530340?versionId=829859&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247429"
            }
         ],
         "id": 247429,
         "name": "PVT_NIC_RSSV6_MULTIMODE_LACP_IFGRP_VLAN",
         "order": 44,
         "pid": "TR-48",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "44"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530340,
            "test_case_version_id": 829859,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44198,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829859,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542695,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542695?versionId=834054&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247430"
            }
         ],
         "id": 247430,
         "name": "PVT_NIC_RSSv6_MTU",
         "order": 45,
         "pid": "TR-49",
         "created_date": "2017-12-14T09:34:31+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "45"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1128184"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542695,
            "test_case_version_id": 834054,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44233,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 834054,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542697,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542697?versionId=834055&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247431"
            }
         ],
         "id": 247431,
         "name": "PVT_NIC_RSSv6_VLAN_MTU",
         "order": 46,
         "pid": "TR-50",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "46"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542697,
            "test_case_version_id": 834055,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44199,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834055,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530516,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530516?versionId=829933&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247432"
            }
         ],
         "id": 247432,
         "name": "PVT_NIC_IPv4_AUTO_IP_CHECKSUM",
         "order": 47,
         "pid": "TR-51",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "47"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530516,
            "test_case_version_id": 829933,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44200,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829933,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 534023,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/534023?versionId=729227&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247433"
            }
         ],
         "id": 247433,
         "name": "PVT_NIC_IPv4_B2B_LOOPBACK",
         "order": 48,
         "pid": "TR-52",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "48"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 534023,
            "test_case_version_id": 729227,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44201,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 729227,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530521,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530521?versionId=829938&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247434"
            }
         ],
         "id": 247434,
         "name": "PVT_NIC_Opr_AUTO_SINGLE_PORT_LINK",
         "order": 49,
         "pid": "TR-53",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "49"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530521,
            "test_case_version_id": 829938,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44202,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829938,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530539,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530539?versionId=829956&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247435"
            }
         ],
         "id": 247435,
         "name": "PVT_NIC_MTU_AUTO_VARIOUS",
         "order": 50,
         "pid": "TR-54",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "50"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530539,
            "test_case_version_id": 829956,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44203,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829956,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530540,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530540?versionId=829957&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247436"
            }
         ],
         "id": 247436,
         "name": "PVT_NIC_MTU_AUTO_VARIOUS_VLAN",
         "order": 51,
         "pid": "TR-55",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "51"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530540,
            "test_case_version_id": 829957,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44204,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829957,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 746280,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/746280?versionId=1012904&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247437"
            }
         ],
         "id": 247437,
         "name": "PVT_NIC_MTU_Jumbo_Rx_Tx",
         "order": 52,
         "pid": "TR-56",
         "created_date": "2017-12-14T09:34:58+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "52"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1125326"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 746280,
            "test_case_version_id": 1012904,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44234,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 1012904,
         "test_case_version": "1.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542703,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542703?versionId=834056&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247438"
            }
         ],
         "id": 247438,
         "name": "PVT_NIC_VLAN_Toggle",
         "order": 53,
         "pid": "TR-57",
         "created_date": "2017-12-14T09:24:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "53"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542703,
            "test_case_version_id": 834056,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44205,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834056,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542707,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542707?versionId=834059&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247439"
            }
         ],
         "id": 247439,
         "name": "PVT_NIC_VLAN_Create_Delete",
         "order": 54,
         "pid": "TR-58",
         "created_date": "2017-12-14T09:35:18+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "54"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1121420"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542707,
            "test_case_version_id": 834059,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44235,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 834059,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530623,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530623?versionId=829977&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247440"
            }
         ],
         "id": 247440,
         "name": "PVT_NIC_TSO_VLAN",
         "order": 55,
         "pid": "TR-59",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "55"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530623,
            "test_case_version_id": 829977,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44206,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 829977,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542653,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542653?versionId=834037&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247441"
            }
         ],
         "id": 247441,
         "name": "PVT_NIC_TSO_MTU",
         "order": 56,
         "pid": "TR-60",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "56"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542653,
            "test_case_version_id": 834037,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44207,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834037,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542662,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542662?versionId=834041&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247442"
            }
         ],
         "id": 247442,
         "name": "PVT_NIC_TSO_VLAN_MTU",
         "order": 57,
         "pid": "TR-61",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "57"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542662,
            "test_case_version_id": 834041,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44208,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834041,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542665,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542665?versionId=834043&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247443"
            }
         ],
         "id": 247443,
         "name": "PVT_NIC_TSO_Multimode_LACP_Ifgrp_VLAN",
         "order": 58,
         "pid": "TR-62",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "58"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542665,
            "test_case_version_id": 834043,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44209,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 834043,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 534018,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/534018?versionId=831804&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247444"
            }
         ],
         "id": 247444,
         "name": "PVT_NIC_IPv6_Ping6_Test",
         "order": 59,
         "pid": "TR-63",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "59"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 534018,
            "test_case_version_id": 831804,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44210,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 831804,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538156,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538156?versionId=832712&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247445"
            }
         ],
         "id": 247445,
         "name": "PVT_NIC_LROv6_Singlemode_Ifgrp",
         "order": 60,
         "pid": "TR-64",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "60"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538156,
            "test_case_version_id": 832712,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44211,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 832712,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538159,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538159?versionId=832715&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247446"
            }
         ],
         "id": 247446,
         "name": "PVT_NIC_LROv6_Ifgrp_Multimode_LACP_Over_VLAN",
         "order": 61,
         "pid": "TR-65",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "61"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538159,
            "test_case_version_id": 832715,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44212,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 832715,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538160,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538160?versionId=832716&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247447"
            }
         ],
         "id": 247447,
         "name": "PVT_NIC_LROv6_VLAN",
         "order": 62,
         "pid": "TR-66",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "62"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538160,
            "test_case_version_id": 832716,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44213,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 832716,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538161,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538161?versionId=832717&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247448"
            }
         ],
         "id": 247448,
         "name": "PVT_NIC_LROv6_MTU",
         "order": 63,
         "pid": "TR-67",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "63"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538161,
            "test_case_version_id": 832717,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44214,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 832717,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540690,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540690?versionId=833468&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247449"
            }
         ],
         "id": 247449,
         "name": "PVT_NIC_LROv6_LROv4_NFS_Integration",
         "order": 64,
         "pid": "TR-68",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "64"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540690,
            "test_case_version_id": 833468,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44215,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 833468,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543312,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543312?versionId=734733&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247450"
            }
         ],
         "id": 247450,
         "name": "PVT_NIC_LED_100G_link",
         "order": 65,
         "pid": "TR-69",
         "created_date": "2017-12-14T09:24:39+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "65"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543312,
            "test_case_version_id": 734733,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44216,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734733,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543313,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543313?versionId=734734&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247451"
            }
         ],
         "id": 247451,
         "name": "PVT_NIC_LED_100G_Activity",
         "order": 66,
         "pid": "TR-70",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "66"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543313,
            "test_case_version_id": 734734,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44217,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734734,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543317,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543317?versionId=734735&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247452"
            }
         ],
         "id": 247452,
         "name": "PVT_NIC_QSFP28_QSFP_Hotswap_traffic",
         "order": 67,
         "pid": "TR-71",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "67"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543317,
            "test_case_version_id": 734735,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44218,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734735,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542413,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542413?versionId=734000&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247453"
            }
         ],
         "id": 247453,
         "name": "PVT_NIC_misc_counter_manager",
         "order": 68,
         "pid": "TR-72",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "68"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542413,
            "test_case_version_id": 734000,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44219,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734000,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542423,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542423?versionId=989731&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247454"
            }
         ],
         "id": 247454,
         "name": "PVT_NIC_misc_NIC_Link_Status",
         "order": 69,
         "pid": "TR-73",
         "created_date": "2017-12-14T09:35:58+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "69"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120139"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542423,
            "test_case_version_id": 989731,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44236,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 989731,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542522,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542522?versionId=734084&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247455"
            }
         ],
         "id": 247455,
         "name": "PVT_NIC_misc_ifstat_link_up_down_speed_check",
         "order": 70,
         "pid": "TR-74",
         "created_date": "2017-12-14T09:36:29+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "70"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120144"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542522,
            "test_case_version_id": 734084,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44237,
            "exe_start_date": "2017-12-14T09:38:36+00:00",
            "exe_end_date": "2017-12-14T09:38:36+00:00"
         },
         "test_case_version_id": 734084,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 534015,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/534015?versionId=729182&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247456"
            }
         ],
         "id": 247456,
         "name": "NIC_L2ping_BASIC",
         "order": 71,
         "pid": "TR-75",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "71"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 534015,
            "test_case_version_id": 729182,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44220,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 729182,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543027,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543027?versionId=734542&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247457"
            }
         ],
         "id": 247457,
         "name": "PVT_NIC_CIFS",
         "order": 72,
         "pid": "TR-76",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "72"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543027,
            "test_case_version_id": 734542,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44221,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734542,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543039,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543039?versionId=734544&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247458"
            }
         ],
         "id": 247458,
         "name": "PVT_NIC_iSCSI",
         "order": 73,
         "pid": "TR-77",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "73"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543039,
            "test_case_version_id": 734544,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44222,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734544,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543040,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543040?versionId=660207&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247459"
            }
         ],
         "id": 247459,
         "name": "PVT_NIC_iSCSI_VLAN",
         "order": 74,
         "pid": "TR-78",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "74"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543040,
            "test_case_version_id": 660207,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44223,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 660207,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543367,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543367?versionId=734827&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247460"
            }
         ],
         "id": 247460,
         "name": "PVT_NIC_B2B_PingV4 test",
         "order": 75,
         "pid": "TR-79",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "75"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543367,
            "test_case_version_id": 734827,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44224,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734827,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16674,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 543368,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/543368?versionId=734798&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16674"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/247461"
            }
         ],
         "id": 247461,
         "name": "PVT_NIC_B2B_PingV6 test",
         "order": 76,
         "pid": "TR-80",
         "created_date": "2017-12-14T09:24:40+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "76"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 543368,
            "test_case_version_id": 734798,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44225,
            "exe_start_date": "2017-12-14T09:24:34+00:00",
            "exe_end_date": "2017-12-14T09:24:34+00:00"
         },
         "test_case_version_id": 734798,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542688,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542688?versionId=834048&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248509"
            }
         ],
         "id": 248509,
         "name": "PVT_NIC_RSSv4_MTU",
         "order": 1,
         "pid": "TR-81",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "1"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1128184"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542688,
            "test_case_version_id": 834048,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44149,
            "exe_start_date": "2017-12-14T08:54:52+00:00",
            "exe_end_date": "2017-12-14T08:54:52+00:00"
         },
         "test_case_version_id": 834048,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542690,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542690?versionId=834050&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248510"
            }
         ],
         "id": 248510,
         "name": "PVT_NIC_RSSv4_Multimode_Ifgrp_VLAN",
         "order": 2,
         "pid": "TR-82",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "2"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542690,
            "test_case_version_id": 834050,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44131,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 834050,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524860,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524860?versionId=827224&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248511"
            }
         ],
         "id": 248511,
         "name": "PVT_NIC_TSO6_MTU",
         "order": 3,
         "pid": "TR-83",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "3"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524860,
            "test_case_version_id": 827224,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44132,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 827224,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524866,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524866?versionId=689292&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248512"
            }
         ],
         "id": 248512,
         "name": "PVT_NIC_TSO6_Multimode_LACP_Ifgrp",
         "order": 4,
         "pid": "TR-84",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "4"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524866,
            "test_case_version_id": 689292,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44133,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 689292,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524900,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524900?versionId=827236&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248513"
            }
         ],
         "id": 248513,
         "name": "PVT_NIC_LROV4_Multimode_LACP_Ifgrp",
         "order": 5,
         "pid": "TR-85",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "5"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524900,
            "test_case_version_id": 827236,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44134,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 827236,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524907,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524907?versionId=827240&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248514"
            }
         ],
         "id": 248514,
         "name": "PVT_NIC_LROV4_MTU",
         "order": 6,
         "pid": "TR-86",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "6"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524907,
            "test_case_version_id": 827240,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44135,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 827240,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524908,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524908?versionId=827241&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248515"
            }
         ],
         "id": 248515,
         "name": "PVT_NIC_LROV4_VLAN",
         "order": 7,
         "pid": "TR-87",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "7"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524908,
            "test_case_version_id": 827241,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44136,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 827241,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 525744,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/525744?versionId=827890&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248516"
            }
         ],
         "id": 248516,
         "name": "PVT_NIC_LMF_v6_Multicast_large_entries_reboot",
         "order": 8,
         "pid": "TR-88",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "8"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120845"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 525744,
            "test_case_version_id": 827890,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44150,
            "exe_start_date": "2017-12-14T08:54:52+00:00",
            "exe_end_date": "2017-12-14T08:54:52+00:00"
         },
         "test_case_version_id": 827890,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540748,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540748?versionId=733198&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248517"
            }
         ],
         "id": 248517,
         "name": "PVT_NIC_Spirent Unicast 64B Frame",
         "order": 9,
         "pid": "TR-89",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "9"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540748,
            "test_case_version_id": 733198,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44137,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 733198,
         "test_case_version": "2.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530339,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530339?versionId=829858&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248518"
            }
         ],
         "id": 248518,
         "name": "PVT_NIC_RSSV6_MULTIMODE_LACP_IFGRP",
         "order": 10,
         "pid": "TR-90",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "10"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530339,
            "test_case_version_id": 829858,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44138,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 829858,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542695,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542695?versionId=834054&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248519"
            }
         ],
         "id": 248519,
         "name": "PVT_NIC_RSSv6_MTU",
         "order": 11,
         "pid": "TR-91",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "11"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "602",
               "field_value_name": "Failed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": "1120450"
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "44",
               "field_value_name": "PLTE"
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542695,
            "test_case_version_id": 834054,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Failed",
            "id": 44151,
            "exe_start_date": "2017-12-14T08:54:52+00:00",
            "exe_end_date": "2017-12-14T08:54:52+00:00"
         },
         "test_case_version_id": 834054,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530539,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530539?versionId=829956&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248520"
            }
         ],
         "id": 248520,
         "name": "PVT_NIC_MTU_AUTO_VARIOUS",
         "order": 12,
         "pid": "TR-92",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "12"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530539,
            "test_case_version_id": 829956,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44140,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 829956,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530540,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530540?versionId=829957&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248521"
            }
         ],
         "id": 248521,
         "name": "PVT_NIC_MTU_AUTO_VARIOUS_VLAN",
         "order": 13,
         "pid": "TR-93",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "13"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530540,
            "test_case_version_id": 829957,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44141,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 829957,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 530618,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/530618?versionId=829972&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248522"
            }
         ],
         "id": 248522,
         "name": "PVT_NIC_TSO_Multimode_LACP_Ifgrp",
         "order": 14,
         "pid": "TR-94",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "14"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 530618,
            "test_case_version_id": 829972,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44142,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 829972,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542653,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542653?versionId=834037&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248523"
            }
         ],
         "id": 248523,
         "name": "PVT_NIC_TSO_MTU",
         "order": 15,
         "pid": "TR-95",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "15"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542653,
            "test_case_version_id": 834037,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44143,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 834037,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538158,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538158?versionId=832714&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248524"
            }
         ],
         "id": 248524,
         "name": "PVT_NIC_LROv6_Ifgrp_Multimode_LACP",
         "order": 16,
         "pid": "TR-96",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "16"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538158,
            "test_case_version_id": 832714,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44144,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 832714,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16718,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538161,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538161?versionId=832717&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16718"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/248525"
            }
         ],
         "id": 248525,
         "name": "PVT_NIC_LROv6_MTU",
         "order": 17,
         "pid": "TR-97",
         "created_date": "2017-12-04T09:48:15+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "17"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "[118]",
               "field_value_name": "[FAS9000]"
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538161,
            "test_case_version_id": 832717,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 44145,
            "exe_start_date": "2017-12-14T08:51:45+00:00",
            "exe_end_date": "2017-12-14T08:51:45+00:00"
         },
         "test_case_version_id": 832717,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524870,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524870?versionId=827231&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249943"
            }
         ],
         "id": 249943,
         "name": "PVT_NIC_TSO6_Multimode_LACP_Ifgrp_VLAN",
         "order": 1,
         "pid": "TR-98",
         "created_date": "2017-12-11T06:59:51+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "1"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524870,
            "test_case_version_id": 827231,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42801,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 827231,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524897,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524897?versionId=827234&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249944"
            }
         ],
         "id": 249944,
         "name": "PVT_NIC_LROV4_Singlemode_Ifgrp",
         "order": 2,
         "pid": "TR-99",
         "created_date": "2017-12-11T07:02:38+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "2"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524897,
            "test_case_version_id": 827234,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42802,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 827234,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524908,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524908?versionId=827241&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249945"
            }
         ],
         "id": 249945,
         "name": "PVT_NIC_LROV4_VLAN",
         "order": 3,
         "pid": "TR-100",
         "created_date": "2017-12-11T07:02:30+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "3"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524908,
            "test_case_version_id": 827241,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42803,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 827241,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 524909,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/524909?versionId=827242&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249946"
            }
         ],
         "id": 249946,
         "name": "PVT_NIC_LROV4_Multimode_LACP_Ifgrp_VLAN",
         "order": 4,
         "pid": "TR-101",
         "created_date": "2017-12-11T07:02:49+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "4"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 524909,
            "test_case_version_id": 827242,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42804,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 827242,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 538160,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/538160?versionId=832716&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249947"
            }
         ],
         "id": 249947,
         "name": "PVT_NIC_LROv6_VLAN",
         "order": 5,
         "pid": "TR-102",
         "created_date": "2017-12-11T07:02:59+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "5"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 538160,
            "test_case_version_id": 832716,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42805,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 832716,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 540690,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/540690?versionId=833468&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249948"
            }
         ],
         "id": 249948,
         "name": "PVT_NIC_LROv6_LROv4_NFS_Integration",
         "order": 6,
         "pid": "TR-103",
         "created_date": "2017-12-11T07:03:10+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "6"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 540690,
            "test_case_version_id": 833468,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42806,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 833468,
         "test_case_version": "3.0",
         "creator_id": 473
      },
      {
         "parentId": 16643,
         "parentType": "test-suite",
         "automation": "No",
         "testCaseId": 542493,
         "links": [
            {
               "rel": "test-case",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cases/542493?versionId=734110&showParamIdentifier=false"
            },
            {
               "rel": "test-cycle",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-cycles/6684"
            },
            {
               "rel": "test-suite",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-suites/16643"
            },
            {
               "rel": "self",
               "href": "https://qtest.eng.netapp.com/api/v3/projects/67/test-runs/249949"
            }
         ],
         "id": 249949,
         "name": "PVT_NIC_ifgrp_port_down_check_ems",
         "order": 7,
         "pid": "TR-104",
         "created_date": "2017-12-11T07:03:23+00:00",
         "last_modified_date": "2021-03-18T10:24:44+00:00",
         "properties": [
            {
               "field_id": 7096,
               "field_name": "Run Order",
               "field_value": "7"
            },
            {
               "field_id": 7086,
               "field_name": "Execution Type",
               "field_value": "501",
               "field_value_name": "Functional"
            },
            {
               "field_id": 7094,
               "field_name": "Planned Start Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7097,
               "field_name": "Status",
               "field_value": "601",
               "field_value_name": "Passed"
            },
            {
               "field_id": 7093,
               "field_name": "Planned End Date",
               "field_value": "2017-10-27T00:00:00+00:00"
            },
            {
               "field_id": 7101,
               "field_name": "Build Version",
               "field_value": ""
            },
            {
               "field_id": 7077,
               "field_name": "Assigned To",
               "field_value": "473",
               "field_value_name": "Amit Haval"
            },
            {
               "field_id": 7102,
               "field_name": "Controllers Used",
               "field_value": ""
            },
            {
               "field_id": 7103,
               "field_name": "BURT",
               "field_value": ""
            },
            {
               "field_id": 7104,
               "field_name": "Incidents",
               "field_value": ""
            },
            {
               "field_id": 10950,
               "field_name": "Runtime",
               "field_value": ""
            },
            {
               "field_id": 10980,
               "field_name": "Time To First Failure",
               "field_value": ""
            },
            {
               "field_id": 11010,
               "field_name": "Expected Runtime",
               "field_value": ""
            },
            {
               "field_id": 7138,
               "field_name": "Keywords",
               "field_value": ""
            },
            {
               "field_id": 7108,
               "field_name": "Systemic Ratchet Level",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7109,
               "field_name": "NATE LOG URL",
               "field_value": ""
            },
            {
               "field_id": 7139,
               "field_name": "ONTAP Mode",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7110,
               "field_name": "Pass Rate",
               "field_value": ""
            },
            {
               "field_id": 7140,
               "field_name": "Executing Subteam",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7141,
               "field_name": "Product Models",
               "field_value": "",
               "field_value_name": ""
            },
            {
               "field_id": 7111,
               "field_name": "QC_APP_NAME",
               "field_value": ""
            },
            {
               "field_id": 7112,
               "field_name": "Duration",
               "field_value": ""
            },
            {
               "field_id": 7114,
               "field_name": "NATE_UUID",
               "field_value": ""
            },
            {
               "field_id": 7115,
               "field_name": "Description",
               "field_value": ""
            },
            {
               "field_id": 7113,
               "field_name": "ZAPI Input",
               "field_value": ""
            },
            {
               "field_id": 17618,
               "field_name": "CTL Execution ID",
               "field_value": ""
            },
            {
               "field_id": 17619,
               "field_name": "SITE",
               "field_value": ""
            },
            {
               "field_id": 17620,
               "field_name": "NATE TOP LOGDIR",
               "field_value": ""
            }
         ],
         "test_case": {
            "links": [],
            "id": 542493,
            "test_case_version_id": 734110,
            "agent_ids": []
         },
         "latest_test_log": {
            "status": "Passed",
            "id": 42807,
            "exe_start_date": "2017-12-11T09:39:07+00:00",
            "exe_end_date": "2017-12-11T09:39:07+00:00"
         },
         "test_case_version_id": 734110,
         "test_case_version": "2.0",
         "creator_id": 473
      }
   ]}


    
    data_header = ["ID", "NAME", "STATUS", "TYPE", "VERSION","LAST MODIFED DATE"]
    return data123['items'], data_header


               
def home(request):
    if request.method == 'POST':
        query = request.POST.get('query_select')
        if query == 'burt':
            num_of_tables = request.POST.get('num_of_tables')
            number_of_rows = request.POST.get('number_of_rows')
            number_of_columns = request.POST.get('number_of_columns')
            return redirect(f'/query_boss/{num_of_tables}/{number_of_rows}/{number_of_columns}')
        elif query == 'Jira':
            pass
        elif query == 'QTest':
            return redirect('q_test')
    else:
        return render(request, 'burt/home.html')
        
def q_test(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get('query')
    data, data_header = QTestHandler(query)

    return render(request, 'burt/QTest.html', {"data":data, "header": data_header, "query": query})

from .models import TempDataHolder
def query_boss(request, num_of_tables, number_of_rows, number_of_columns):
    if request.method == 'POST':
        keywords = []
        main_keywords = []
        for i in range(int(num_of_tables)):
            for j in range(number_of_columns):
                keywords.append(request.POST.get(f'keyword{i+1}{j}'))
            for j in range(number_of_rows):
                main_keywords.append(request.POST.get(f'mainkeyword{i+1}{j}key'))
            tdh = TempDataHolder()
            one = ''
            two = ''
        print(main_keywords, 'main_keywords')
        for item in keywords:
            one = one + str(item) + ','
        for item in main_keywords:
            two = two + str(item) + ','
        
        # saving it to database for future use
        tdh.keywords = one
        tdh.main_keywords = two
        tdh.save()

        context = {
            'pk': tdh.pk,
            'list_': range(num_of_tables),
            'number_of_rows': range(number_of_rows),
            'number_of_columns': range(number_of_columns),
            'num_of_tables': num_of_tables,
            'number_of_rows_1': number_of_rows,
            'number_of_columns1': number_of_columns,
            'number_of_input_box': range(number_of_rows * number_of_columns),
            'previous_data_pk': tdh.pk

        }
        return render(request, 'burt/show_queries_input.html', context)

    else:
        context = {
            'list_': range(num_of_tables),
            'number_of_rows': range(number_of_rows),
            'number_of_columns': range(number_of_columns),
            'num_of_tables': num_of_tables,
            'number_of_rows_1': number_of_rows,
            'number_of_columns1': number_of_columns
        }
        return render(request, 'burt/query_boss.html', context)



def new_query_boss(request, number_of_tables, number_of_rows, number_of_columns, previous_data_pk):
    if request.method == 'POST':
        query_set = []
        results = []
        keywords = TempDataHolder.objects.get(pk = previous_data_pk).keywords.split(',')[0:-1]
        keywords = [keywords[i:i+number_of_columns] for i in range(0, len(keywords), number_of_columns)]
        
        names = TempDataHolder.objects.get(pk = previous_data_pk).main_keywords.split(',')[0:-1]
        names = [names[i:i+number_of_rows] for i in range(0, len(names), number_of_rows)]
        new = []
        
        for i in range(number_of_tables):
          for j in range(number_of_rows):
            for k in range(number_of_columns):
              query = request.POST.get(f'q{i}{j}{k}')
              print(query, i, j, k)
              result = send_req_get_data(query)
                      
              results.append(result)
        results = [results[i:i+number_of_columns] for i in range(0, len(results), number_of_columns)]
        x = 0
        for v, z in zip(keywords, results):
          tmp_list = {
            "data": []
          }
          for word in v:
            print(word)
            tmp_dict = {}
            for result in z:
              tmp = result.lower().count(word.lower())
              print(result, word, tmp)
              if tmp_dict and tmp_dict["name"] == word:
                tmp_dict["value"] += tmp
              else:
                tmp_dict["name"] = word
                tmp_dict["value"] = tmp
            try:
              tmp_list["word"] = names[x][0]
            except:
              tmp_list["word"] = ''
            tmp_list["data"].append(tmp_dict)
          new.append(tmp_list)
          x += 1
                    
        print(new)
        print(keywords)
        context = {
            'results': results,
            'result': new,
            'keywords': keywords
        }
        return render(request, 'burt/burt_new_result.html', context)

        # keywords = []
        # for i in range(number_of_columns):
        #     keywords.append(request.POST.get(f'keyword{i}'))
        # names = []
        # new = []
        # for i in range(int(number_of_tables)):
        #     name = request.POST.get(f'name_{i+1}')

        #     query_ = request.POST.get(f'q_{i+1}')
        #     print(query_)

        #     # counting for every keyword then keeping the result inside res dict
        #     result = send_req_get_data(query_).lower()
        #     print('result: '+result)
        #     tmp_dict = {}
        #     for word in keywords:
        #         tmp = result.count(word.lower())
        #         tmp_dict[f'{word}'] = tmp
        #     if name not in names:
        #         names.append(name)
        #         new.append([name, tmp_dict])
        #     else:
        #         for item in new:
        #             if name in item[0]:
        #                 for w in keywords:
        #                     item[1][w] = item[1][w] + tmp_dict[w]
        #                 break
    else:
        pass


def burt_(request):
    if request.method == 'POST':
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')
        

        if 'submit' in request.POST:
            open_new = send_req_get_data(open_new).lower()
            test_me = send_req_get_data(test_me).lower()
            study = send_req_get_data(study).lower()
            fixed = send_req_get_data(fixed).lower()
            closed = send_req_get_data(closed).lower()
            multistate = send_req_get_data(multistate).lower()

            # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate     
            Dg2Au = [0, 0, 0, 0, 0, 0]    
            Dg2Au[0] =  Dg2Au[0] + open_new.count('new')
            Dg2Au[0] =  Dg2Au[0] + open_new.count('open')
            Dg2Au[1] =  Dg2Au[1] + open_new.count('testme')
            Dg2Au[2] =  Dg2Au[2] + open_new.count('study')
            Dg2Au[3] =  Dg2Au[3] + open_new.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + open_new.count('closed')
            Dg2Au[5] =  Dg2Au[5] + open_new.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + test_me.count('new')
            Dg2Au[0] =  Dg2Au[0] + test_me.count('open')
            Dg2Au[1] =  Dg2Au[1] + test_me.count('testme')
            Dg2Au[2] =  Dg2Au[2] + test_me.count('study')
            Dg2Au[3] =  Dg2Au[3] + test_me.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + test_me.count('closed')
            Dg2Au[5] =  Dg2Au[5] + test_me.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + study.count('new')
            Dg2Au[0] =  Dg2Au[0] + study.count('open')
            Dg2Au[1] =  Dg2Au[1] + study.count('testme')
            Dg2Au[2] =  Dg2Au[2] + study.count('study')
            Dg2Au[3] =  Dg2Au[3] + study.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + study.count('closed')
            Dg2Au[5] =  Dg2Au[5] + study.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + fixed.count('new')
            Dg2Au[0] =  Dg2Au[0] + fixed.count('open')
            Dg2Au[1] =  Dg2Au[1] + fixed.count('testme')
            Dg2Au[2] =  Dg2Au[2] + fixed.count('study')
            Dg2Au[3] =  Dg2Au[3] + fixed.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + fixed.count('closed')
            Dg2Au[5] =  Dg2Au[5] + fixed.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + closed.count('new')
            Dg2Au[0] =  Dg2Au[0] + closed.count('open')
            Dg2Au[1] =  Dg2Au[1] + closed.count('testme')
            Dg2Au[2] =  Dg2Au[2] + closed.count('study')
            Dg2Au[3] =  Dg2Au[3] + closed.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + closed.count('closed')
            Dg2Au[5] =  Dg2Au[5] + closed.count('multistate')


            Dg2Au[0] =  Dg2Au[0] + multistate.count('new')
            Dg2Au[0] =  Dg2Au[0] + multistate.count('open')
            Dg2Au[1] =  Dg2Au[1] + multistate.count('testme')
            Dg2Au[2] =  Dg2Au[2] + multistate.count('study')
            Dg2Au[3] =  Dg2Au[3] + multistate.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + multistate.count('closed')
            Dg2Au[5] =  Dg2Au[5] + multistate.count('multistate') 

            # todo: add the same thing for multistate

            obj = HelperModel()
            obj.open_new = Dg2Au[0]
            obj.test_me = Dg2Au[1]
            obj.study = Dg2Au[2]
            obj.fixed = Dg2Au[3]
            obj.closed = Dg2Au[4]
            obj.multistate = Dg2Au[5]
            obj.total = Dg2Au[0] + Dg2Au[1] + Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
            obj.save()
            return redirect(f'/burt2/{obj.pk}')

        elif 'save' in request.POST:
            # save the query in Database
            # obj = QueryHolder()
            # obj.query = query
            # obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')


def burt__(request, pk):
    obj = HelperModel.objects.get(pk=pk)
    if request.method == 'POST':
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')
        open_new = send_req_get_data(open_new).lower()
        test_me = send_req_get_data(test_me).lower()
        study = send_req_get_data(study).lower()
        fixed = send_req_get_data(fixed).lower()
        closed = send_req_get_data(closed).lower()
        multistate = send_req_get_data(multistate).lower()

        # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate     
        Dg2Au = [0, 0, 0, 0, 0, 0]      
        Dg2Au[0] =  Dg2Au[0] + open_new.count('new')
        Dg2Au[0] =  Dg2Au[0] + open_new.count('open')
        Dg2Au[1] =  Dg2Au[1] + open_new.count('testme')
        Dg2Au[2] =  Dg2Au[2] + open_new.count('study')
        Dg2Au[3] =  Dg2Au[3] + open_new.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + open_new.count('closed')
        Dg2Au[5] =  Dg2Au[5] + open_new.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + test_me.count('new')
        Dg2Au[0] =  Dg2Au[0] + test_me.count('open')
        Dg2Au[1] =  Dg2Au[1] + test_me.count('testme')
        Dg2Au[2] =  Dg2Au[2] + test_me.count('study')
        Dg2Au[3] =  Dg2Au[3] + test_me.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + test_me.count('closed')
        Dg2Au[5] =  Dg2Au[5] + test_me.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + study.count('new')
        Dg2Au[0] =  Dg2Au[0] + study.count('open')
        Dg2Au[1] =  Dg2Au[1] + study.count('testme')
        Dg2Au[2] =  Dg2Au[2] + study.count('study')
        Dg2Au[3] =  Dg2Au[3] + study.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + study.count('closed')
        Dg2Au[5] =  Dg2Au[5] + study.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + fixed.count('new')
        Dg2Au[0] =  Dg2Au[0] + fixed.count('open')
        Dg2Au[1] =  Dg2Au[1] + fixed.count('testme')
        Dg2Au[2] =  Dg2Au[2] + fixed.count('study')
        Dg2Au[3] =  Dg2Au[3] + fixed.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + fixed.count('closed')
        Dg2Au[5] =  Dg2Au[5] + fixed.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + closed.count('new')
        Dg2Au[0] =  Dg2Au[0] + closed.count('open')
        Dg2Au[1] =  Dg2Au[1] + closed.count('testme')
        Dg2Au[2] =  Dg2Au[2] + closed.count('study')
        Dg2Au[3] =  Dg2Au[3] + closed.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + closed.count('closed')
        Dg2Au[5] =  Dg2Au[5] + closed.count('multistate')


        Dg2Au[0] =  Dg2Au[0] + multistate.count('new')
        Dg2Au[0] =  Dg2Au[0] + multistate.count('open')
        Dg2Au[1] =  Dg2Au[1] + multistate.count('testme')
        Dg2Au[2] =  Dg2Au[2] + multistate.count('study')
        Dg2Au[3] =  Dg2Au[3] + multistate.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + multistate.count('closed')
        Dg2Au[5] =  Dg2Au[5] + multistate.count('multistate')        
        total = Dg2Au[0] + Dg2Au[1] + Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
        # todo: add the same thing for multistate
        context = {
            'dg2au': obj,
            'open_new': Dg2Au[0],
            'test_me': Dg2Au[1],
            'study': Dg2Au[2],
            'fixed': Dg2Au[3],
            'closed': Dg2Au[4],
            'multistate': Dg2Au[5],
            'total1': obj.total,
            'total2': total
        }
        return render(request, 'burt/result.html', context)
    else:
        return render(request, 'burt/burt2.html')

# ----helpers---
def send_req_get_data(query):
    import paramiko

    host = "10.140.60.54"
    username = ""
    password = ""

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout,_stderr = client.exec_command(query)
    x = _stdout.read().decode()
    client.close()
    return x