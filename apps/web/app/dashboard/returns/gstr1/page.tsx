"use client"

import { useState, useEffect } from "react"

// Mock Data Type
type GSTR1Summary = {
    gstin: string
    fp: string
    b2b: any[]
}

export default function GSTR1Page() {
    const [data, setData] = useState<GSTR1Summary | null>(null)

    useEffect(() => {
        // Fetch data from API
        // fetch('http://localhost:8000/returns/gstr1?gstin=...&period=...')

        // Mock Response
        setData({
            gstin: "27ABCDE1234F1Z5",
            fp: "082025",
            b2b: [
                {
                    ctin: "27ABCDE1234F1Z5",
                    inv_no: "INV-001",
                    inv_dt: "01-08-2025",
                    val: 1180.00,
                    pos: "27",
                    tax_val: 1000.00,
                    rt: 18.0,
                    camt: 90.0,
                    samt: 90.0
                }
            ]
        })
    }, [])

    if (!data) return <div>Loading...</div>

    return (
        <div className="container mx-auto py-10">
            <h1 className="text-2xl font-bold mb-5">GSTR-1: {data.fp}</h1>

            <div className="mb-8">
                <h2 className="text-xl font-semibold mb-3">4A, 4B, 4C, 6B, 6C - B2B Invoices</h2>
                <div className="overflow-x-auto">
                    <table className="min-w-full border text-sm">
                        <thead className="bg-gray-100 dark:bg-zinc-800">
                            <tr>
                                <th className="border p-2">GSTIN/UIN</th>
                                <th className="border p-2">Invoice No</th>
                                <th className="border p-2">Date</th>
                                <th className="border p-2">Value</th>
                                <th className="border p-2">Taxable Value</th>
                                <th className="border p-2">Rate</th>
                                <th className="border p-2">IGST</th>
                                <th className="border p-2">CGST</th>
                                <th className="border p-2">SGST</th>
                            </tr>
                        </thead>
                        <tbody>
                            {data.b2b.map((item, idx) => (
                                <tr key={idx}>
                                    <td className="border p-2">{item.ctin}</td>
                                    <td className="border p-2">{item.inv_no}</td>
                                    <td className="border p-2">{item.inv_dt}</td>
                                    <td className="border p-2">{item.val}</td>
                                    <td className="border p-2">{item.tax_val}</td>
                                    <td className="border p-2">{item.rt}%</td>
                                    <td className="border p-2">{item.iamt || 0}</td>
                                    <td className="border p-2">{item.camt || 0}</td>
                                    <td className="border p-2">{item.samt || 0}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}
