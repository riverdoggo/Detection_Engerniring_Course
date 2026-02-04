# Process Tree Abuse

## High Risk Relationships
- Word.exe -> cmd.exe
- Excel.exe -> powershell.exe
- explorer.exe -> rundll32.exe
- mshta.exe -> powershell.exe
- winword.exe -> wscript.exe
- powershell.exe -> net.exe
- cmd.exe -> reg.exe
- outlook.exe -> cmd.exe

## Command Line Indicators
- Encoded PowerShell commands
- Download strings
- Execution from temp paths
- Use of LOLBins
- Base64 arguments
- Hidden window flags
- Script execution flags

## Pseudo Detection – Execution
SELECT * FROM processes
WHERE parent_process IN ('winword.exe','excel.exe')
AND process_name IN ('powershell.exe','cmd.exe');

## Post Execution Abuse
SELECT * FROM processes
WHERE process_name='rundll32.exe'
AND command_line LIKE '%http%';

## False Positives
Allow lists for admin tools and developer machines.
