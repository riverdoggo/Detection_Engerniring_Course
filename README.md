# Detection Engineering & Cloud Security Architecture

## Course Overview

This course is a hands-on, design-driven program focused on **modern detection engineering** for cloud environments.  
Rather than emphasizing tool usage or dashboard interaction, the course teaches students how to **think like a detection engineer**: reasoning from attacker behavior, mapping it to telemetry, designing high-signal detections, and building automation-ready security systems.

The primary environment of focus is **Microsoft Azure**, with an emphasis on **control-plane abuse**, **alert ingestion**, and **SOC-as-Code principles**. The course deliberately avoids reliance on a live cloud subscription, teaching detection design from **documented telemetry contracts and threat models**, mirroring how real-world detection engineering teams operate.

---

## End Goal of the Course

By the end of the course, the student will have:

- Designed a **complete cloud detection strategy** covering identity abuse, network exposure, and high-value resource manipulation
- Built a **vendor-independent alert ingestion pipeline** capable of receiving, validating, deduplicating, and storing security alerts
- Mapped detections to **MITRE ATT&CK** and validated them against realistic cloud attack kill chains
- Produced a **portfolio-grade Git repository** documenting detections, severity models, enrichment strategy, and operational thinking
- Developed the mindset required to transition from *log analysis* to **detection engineering and security architecture**

This course prepares the student for:
- SOC analyst roles with cloud specialization
- Junior detection engineering positions
- Cloud security engineering internships
- Advanced incident response and threat detection work

---

## Weekly Breakdown

---

## Week 1 — KQL Fundamentals & Detection Thinking

**Focus:**  
Understanding how raw telemetry becomes signal.

**Key Topics:**
- Kusto Query Language (KQL) fundamentals
- Pipe-based query thinking
- Filtering, projection, aggregation
- Performance-aware querying
- Distinguishing analysis queries from detection queries

**Outcome:**  
Students learn how to shape large volumes of telemetry into meaningful signals and understand that detection engineering is about **intent and signal quality**, not just querying data.

---

## Week 2 — Azure Control-Plane Telemetry

**Focus:**  
Understanding where cloud security signals originate.

**Key Topics:**
- Azure Monitor architecture
- Diagnostic settings and data collection
- AzureActivity as Tier-0 telemetry
- Control-plane vs data-plane events
- High-risk administrative operations

**Outcome:**  
Students learn how cloud attacks manifest **without touching endpoints**, and why control-plane monitoring is critical for cloud security.

---

## Week 3 — Alerting, Webhooks & SOC-as-Code Foundations

**Focus:**  
Bridging detections and automation.

**Key Topics:**
- Azure Monitor alerting model
- Alert-ready KQL design
- Webhook payload analysis
- Building a FastAPI-based alert receiver
- Shared secret authentication
- Deduplication and rate limiting
- Defensive ingestion design

**Outcome:**  
Students build a **real alert ingestion pipeline** capable of receiving and safely handling security alerts, forming the backbone of a SOC-as-Code architecture.

---

## Week 4 — Azure Control-Plane Detection Strategy

**Focus:**  
Designing high-signal detections for real cloud attacks.

**Key Topics:**
- IAM privilege escalation (RBAC abuse)
- Network Security Group (NSG) exposure
- Key Vault and high-value resource protection
- Severity modeling and alert governance
- Alert enrichment and MITRE ATT&CK alignment
- Kill-chain validation and coverage analysis

**Outcome:**  
Students design a **coherent, threat-driven detection strategy** for Azure control-plane abuse, validated against realistic attacker behavior.

---

## Week 5 — Endpoint Telemetry & Host-Based Detection

**Focus:**  
Moving from cloud configuration abuse to host-level visibility.

**Key Topics:**
- Endpoint telemetry fundamentals
- Sysmon deployment and configuration
- Process creation, parent-child relationships
- Living-off-the-Land Binary (LOLBins) detection
- Credential dumping and persistence signals

**Outcome:**  
Students learn how attacker activity inside virtual machines can be detected using structured endpoint telemetry.

---

## Week 6 — Network Telemetry & Lateral Movement

**Focus:**  
Detecting movement and exfiltration that does not rely on malware.

**Key Topics:**
- NSG Flow Logs
- Network-based detection concepts
- Port scanning and brute-force patterns
- East–west traffic analysis
- Early exfiltration indicators

**Outcome:**  
Students expand detections beyond configuration changes to **network behavior**, completing visibility across the cloud stack.

---

## Week 7 — SOC Automation & Visualization

**Focus:**  
Operationalizing detections.

**Key Topics:**
- Microsoft Sentinel analytics rules
- Automation rules and playbooks
- Workbooks and dashboards
- SOC workflow optimization
- Detection lifecycle management

**Outcome:**  
Students learn how detections are deployed, maintained, and visualized in real SOC environments.

---

## Week 8 — Portfolio Finalization & Professional Readiness

**Focus:**  
Turning technical work into a professional asset.

**Key Topics:**
- Documentation polish
- Detection validation
- Git repository organisation
- Explaining detections to non-technical stakeholders
- Career positioning and interview readiness

**Outcome:**  
Students graduate with a **complete, defensible detection engineering portfolio** demonstrating both technical skill and security reasoning.

---

## Final Statement

This course does not aim to produce tool operators.  
It aims to produce **security thinkers** who understand how attackers behave in cloud environments and how to design systems that detect them early, reliably, and at scale.

The emphasis throughout is on:
- signal over noise
- architecture over dashboards
- reasoning over memorization

This mirrors how real-world detection engineering teams operate in modern cloud security environments.
