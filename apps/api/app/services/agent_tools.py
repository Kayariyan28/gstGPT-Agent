from datetime import datetime
from typing import Dict, Any, List
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.invoice import Invoice
from app.models.return_filing import ReturnFiling, ReturnStatus, ReturnType
from app.core.context import last_tool_output

class AgentTools:
    def get_sales_summary(self, period: str) -> Dict[str, Any]:
        """
        Get sales summary for a specific period (e.g., 'October 2023').
        """
        db = SessionLocal()
        try:
            # Parse period (Simplified: Assume user says "October 2023")
            # In real app, robust date parsing is needed.
            # For demo, we'll just query all invoices if parsing fails or implement simple logic
            
            # Query DB for total sales
            total_sales = db.query(func.sum(Invoice.total_amount)).scalar() or 0.0
            total_tax = db.query(func.sum(Invoice.total_tax_amount)).scalar() or 0.0
            count = db.query(Invoice).count()
            
            result = {
                "status": "success",
                "period": period,
                "data": {
                    "total_sales": float(total_sales),
                    "tax_liability": float(total_tax),
                    "invoice_count": count
                },
                "tool_widget": "SalesSummaryCard" # Hint for UI
            }
            last_tool_output.set(result)
            return result
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            db.close()

    def get_tax_liability(self, period: str) -> Dict[str, Any]:
        """
        Get tax liability for a specific period.
        """
        # Re-use sales summary logic for now
        return self.get_sales_summary(period)

    def draft_gstr1(self, period: str) -> Dict[str, Any]:
        """
        Trigger drafting of GSTR-1 for a period.
        """
        db = SessionLocal()
        try:
            # Create a ReturnFiling record
            filing = ReturnFiling(
                gstin="27ABCDE1234F1Z5", # Mock GSTIN
                period=period,
                return_type=ReturnType.GSTR1,
                status=ReturnStatus.DRAFT
            )
            db.add(filing)
            db.commit()
            db.refresh(filing)
            
            result = {
                "status": "success",
                "message": f"GSTR-1 for {period} has been drafted successfully.",
                "link": f"/dashboard/returns/gstr1?period={period}",
                "draft_id": filing.id,
                "tool_widget": "ReturnDraftCard" # Hint for UI
            }
            last_tool_output.set(result)
            return result
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            db.close()

    def check_compliance_status(self) -> Dict[str, Any]:
        """
        Check overall compliance status.
        """
        return {
            "status": "success",
            "pending_returns": ["GSTR-1 (Nov 2023)", "GSTR-3B (Nov 2023)"],
            "alerts": ["GSTIN verification pending for 2 vendors"]
        }

agent_tools = AgentTools()
