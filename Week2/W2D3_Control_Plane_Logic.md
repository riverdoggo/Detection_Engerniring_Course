# Week 2 Day 3 – Control Plane KQL

## Role Assignment Creation
```kql
AzureActivity
| where OperationNameValue == "Microsoft.Authorization/roleAssignments/write"
| where ActivityStatusValue == "Succeeded"
```

## NSG Deletion
```kql
AzureActivity
| where OperationNameValue contains "networkSecurityGroups/delete"
| where ActivityStatusValue == "Succeeded"
```

## NSG Rule Modification
```kql
AzureActivity
| where OperationNameValue contains "securityRules/write"
| where ActivityStatusValue == "Succeeded"
```

## Key Vault Policy Change
```kql
AzureActivity
| where OperationNameValue contains "KeyVault"
| where ActivityStatusValue == "Succeeded"
```

## Diagnostic Settings Tampering
```kql
AzureActivity
| where OperationNameValue contains "diagnosticSettings"
| where ActivityStatusValue == "Succeeded"
```

**Expected Output**
Time, Caller, OperationName, ResourceId, Status