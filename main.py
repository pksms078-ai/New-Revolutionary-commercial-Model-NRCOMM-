from llm.llm_engine import analyze_notice
from human_control.approval_flow import request_approval
from audit.audit_logger import log_action

with open("data/sample-notices/gst_notice_01.txt") as f:
    notice = f.read()

ai_result = analyze_notice(notice)
decision = request_approval(ai_result)

log_action(
    user="CA_Test",
    action="GST Notice Analysis",
    law="Section 73 CGST",
    ai_output=ai_result,
    decision=decision
)
Add end-to-end GST notice analysis flow


