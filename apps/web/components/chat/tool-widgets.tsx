import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowRight, FileText, IndianRupee } from "lucide-react";
import Link from 'next/link';

interface SalesSummaryData {
    total_sales: number;
    tax_liability: number;
    invoice_count: number;
}

interface ReturnDraftData {
    message: string;
    link: string;
    draft_id: number;
}

export function SalesSummaryCard({ data }: { data: SalesSummaryData }) {
    return (
        <Card className="w-full max-w-sm mt-4 bg-white dark:bg-zinc-900 border-zinc-200 dark:border-zinc-800">
            <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-zinc-500 dark:text-zinc-400">
                    Sales Summary
                </CardTitle>
            </CardHeader>
            <CardContent>
                <div className="text-2xl font-bold">
                    ₹{data.total_sales.toLocaleString('en-IN')}
                </div>
                <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">
                    Total Taxable Value
                </p>
                <div className="mt-4 grid grid-cols-2 gap-4">
                    <div className="flex flex-col">
                        <span className="text-[10px] uppercase text-zinc-500 font-semibold">Tax Liability</span>
                        <span className="text-sm font-medium text-red-500">
                            ₹{data.tax_liability.toLocaleString('en-IN')}
                        </span>
                    </div>
                    <div className="flex flex-col">
                        <span className="text-[10px] uppercase text-zinc-500 font-semibold">Invoices</span>
                        <span className="text-sm font-medium">
                            {data.invoice_count}
                        </span>
                    </div>
                </div>
            </CardContent>
        </Card>
    );
}

export function ReturnDraftCard({ data }: { data: ReturnDraftData }) {
    return (
        <Card className="w-full max-w-sm mt-4 bg-white dark:bg-zinc-900 border-green-200 dark:border-green-900/30">
            <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
                <CardTitle className="text-sm font-medium text-green-600 dark:text-green-400">
                    Draft Created
                </CardTitle>
                <FileText className="h-4 w-4 text-green-600 dark:text-green-400" />
            </CardHeader>
            <CardContent>
                <p className="text-sm text-zinc-600 dark:text-zinc-300 mb-4">
                    {data.message}
                </p>
                <Link href={data.link} passHref>
                    <Button size="sm" className="w-full bg-green-600 hover:bg-green-700 text-white">
                        View Draft <ArrowRight className="ml-2 h-4 w-4" />
                    </Button>
                </Link>
            </CardContent>
        </Card>
    );
}

export function ToolWidget({ context }: { context: any }) {
    if (!context || !context.tool_widget) return null;

    switch (context.tool_widget) {
        case 'SalesSummaryCard':
            return <SalesSummaryCard data={context.data} />;
        case 'ReturnDraftCard':
            return <ReturnDraftCard data={context} />;
        default:
            return null;
    }
}
