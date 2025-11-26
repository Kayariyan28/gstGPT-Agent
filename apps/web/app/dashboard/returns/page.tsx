import Link from "next/link"

export default function ReturnsDashboard() {
    const periods = ["August 2025", "July 2025", "June 2025"]

    return (
        <div className="container mx-auto py-10">
            <h1 className="text-2xl font-bold mb-5">Returns Dashboard</h1>
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                {periods.map((period) => (
                    <div key={period} className="p-6 border rounded-lg shadow-sm hover:shadow-md transition-shadow">
                        <h2 className="text-xl font-semibold mb-2">{period}</h2>
                        <div className="flex flex-col gap-2">
                            <Link
                                href="/dashboard/returns/gstr1"
                                className="text-blue-600 hover:underline"
                            >
                                View GSTR-1 (Outward Supplies)
                            </Link>
                            <Link
                                href="/dashboard/returns/gstr3b"
                                className="text-blue-600 hover:underline"
                            >
                                View GSTR-3B (Summary Return)
                            </Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
