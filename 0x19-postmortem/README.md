## Postmortem

  - A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:
        * To provide the rest of the company’s employees easy access to information detailing the cause of the outage.        * And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Issue Summary

- **Duration:**
    - Start Time: March 20, 2023, 12:30 (UTC)
    - End Time: March 20, 2023, 14:15 (UTC)
- **Impact:**
    - The web service experienced downtime, which cause connection errors for users.
    - 15% of users were affected during inspection
    - The problem was in Nginx server was down which cause the users attempting to access the web server.
- **Root cause:**
    - The absence of a symbolic link between the sites-available and sites-enabled directories prevented Nginx from properly serving content on port 80.

## Timeline

- **Time isssue:**
    - The issue was detected on March 20, 2023, 12:30 (UTC) by automated monitoring alerts.
- **Actions Taken:**
    - Check error file log, and syntax Errors, because the configuration file consist of various directives and must be declared correctly
- **Misleading Paths:**
    - Initially explored database connections, suspecting issues with query performance.
    - Checked for recent code changes in the deployed version.
- **Resolution:**
    - Restore back to the previous version of the application.

## Root Cause and Resolution

- **Root Cause:**
    - A recent code deployment introduced an unforeseen bug, causing the application to crash under certain conditions- **Resolution:**
    - Restore back the previous version 
    - Add automated testing for edge cases to prevent the same issue in future

## Corrective and Preventative Measures

- Add automated tests for more scenarios
- Improve monitoring for the performance of the application
- Review the deployment process thoroughly to ensure that code changes undergo sufficient testing before being released.
- Set up regular checks of the application's error logs to catch potential issues before they escalate.
- Introduce a validation step after deployment to confirm that the application remains stable.
