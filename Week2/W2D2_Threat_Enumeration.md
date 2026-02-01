# Week 2 Day 2 – High Signal Activity Log Events

| Event | Operation Name | Why Defender Cares |
|-----|---------------|--------------------|
| Role Assignment Created | Microsoft.Authorization/roleAssignments/write | Privilege escalation |
| Role Assignment Deleted | Microsoft.Authorization/roleAssignments/delete | Covering tracks |
| NSG Deleted | Microsoft.Network/networkSecurityGroups/delete | Network exposure |
| NSG Rule Modified | Microsoft.Network/networkSecurityGroups/securityRules/write | Backdoor traffic |
| Key Vault Access Policy Changed | Microsoft.KeyVault/vaults/accessPolicies/write | Secret theft |
| Key Vault Deleted | Microsoft.KeyVault/vaults/delete | Data destruction |
| Subscription Policy Removed | Microsoft.Authorization/policyAssignments/delete | Governance bypass |
| Resource Lock Removed | Microsoft.Authorization/locks/delete | Defense removal |
| VM Extension Added | Microsoft.Compute/virtualMachines/extensions/write | Persistence |
| Diagnostic Settings Changed | Microsoft.Insights/diagnosticSettings/write | Blinding detection |