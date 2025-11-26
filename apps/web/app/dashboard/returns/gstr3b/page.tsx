"use client"

import { useState, useEffect } from "react"

type GSTR3BSummary = {
    gstin: string
    fp: string
    sup_details: {
        txval: number
        iamt: number
        camt: number
        samt: number
        csamt: number
    }
    itc_elg: {
        iamt: number
        camt: number
        samt: number
        csamt: number
    }
}

export default function GSTR3BPage() {
    const [data, setData] = useState<GSTR3BSummary | null>(null)

    useEffect(() => {
        // Mock Response
        setData({
            gstin: "27ABCDE1234F1Z5",
            fp: "082025",
            sup_details: {
                txval: 10000.00,
                iamt: 0.0,
                camt: 900.0,
                samt: 900.0,
                csamt: 0.0
            },
            itc_elg: {
                iamt: 500.0,
                camt: 250.0,
                samt: 250.0,
                csamt: 0.0
            }
        })
    }, [])

    if (!data) return <div>Loading...</div>

    return (
        <div className="container mx-auto py-10">
            <h1 className="text-2xl font-bold mb-5">GSTR-3B: {data.fp}</h1>

            <div className="mb-8">
                <h2 className="text-xl font-semibold mb-3">3.1 Details of Outward Supplies</h2>
                <table className="min-w-full border text-sm">
                    <thead className="bg-gray-100 dark:bg-zinc-800">
                        <tr>
                            <th className="border p-2 text-left">Nature of Supplies</th>
                            <th className="border p-2">Taxable Value</th>
                            <th className="border p-2">IGST</th>
                            <th className="border p-2">CGST</th>
                            <th className="border p-2">SGST</th>
                            <th className="border p-2">Cess</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className="border p-2">(a) Outward taxable supplies</td>
                            <td className="border p-2 text-right">{data.sup_details.txval}</td>
                            <td className="border p-2 text-right">{data.sup_details.iamt}</td>
                            <td className="border p-2 text-right">{data.sup_details.camt}</td>
                            <td className="border p-2 text-right">{data.sup_details.samt}</td>
                            <td className="border p-2 text-right">{data.sup_details.csamt}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div className="mb-8">
                <h2 className="text-xl font-semibold mb-3">4. Eligible ITC</h2>
                <table className="min-w-full border text-sm">
                    <thead className="bg-gray-100 dark:bg-zinc-800">
                        <tr>
                            <th className="border p-2 text-left">Details</th>
                            <th className="border p-2">IGST</th>
                            <th className="border p-2">CGST</th>
                            <th className="border p-2">SGST</th>
                            <th className="border p-2">Cess</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className="border p-2">(A) ITC Available (whether in full or part)</td>
                            <td className="border p-2 text-right">{data.itc_elg.iamt}</td>
                            <td className="border p-2 text-right">{data.itc_elg.camt}</td>
                            <td className="border p-2 text-right">{data.itc_elg.samt}</td>
                            <td className="border p-2 text-right">{data.itc_elg.csamt}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}
