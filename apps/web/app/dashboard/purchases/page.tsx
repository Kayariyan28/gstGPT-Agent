"use client"

import { DataTable } from "@/components/ui/data-table"
import { ColumnDef } from "@tanstack/react-table"

export type Purchase = {
    id: string
    invoice_no: string
    vendor: string
    amount: number
    status: "matched" | "mismatch" | "missing"
}

export const columns: ColumnDef<Purchase>[] = [
    {
        accessorKey: "invoice_no",
        header: "Invoice No",
    },
    {
        accessorKey: "vendor",
        header: "Vendor",
    },
    {
        accessorKey: "amount",
        header: "Amount",
    },
    {
        accessorKey: "status",
        header: "Recon Status",
    },
]

const data: Purchase[] = [
    {
        id: "1",
        invoice_no: "INV-001",
        vendor: "ABC Corp",
        amount: 5000,
        status: "matched",
    },
    {
        id: "2",
        invoice_no: "INV-002",
        vendor: "XYZ Ltd",
        amount: 12000,
        status: "mismatch",
    },
]

export default function PurchasePage() {
    return (
        <div className="container mx-auto py-10">
            <h1 className="text-2xl font-bold mb-5">Purchase Register (GSTR-2B)</h1>
            <DataTable columns={columns} data={data} />
        </div>
    )
}
