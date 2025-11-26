"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import { ArrowRight, CheckCircle2, FileText, MessageSquare, ShieldCheck, Zap } from "lucide-react";

export default function LandingPage() {
    const fadeIn = {
        initial: { opacity: 0, y: 20 },
        animate: { opacity: 1, y: 0 },
        transition: { duration: 0.5 }
    };

    const stagger = {
        animate: {
            transition: {
                staggerChildren: 0.1
            }
        }
    };

    return (
        <div className="min-h-screen bg-slate-950 text-slate-50 font-sans selection:bg-emerald-500/30">
            {/* Navbar */}
            <nav className="fixed top-0 w-full z-50 border-b border-slate-800 bg-slate-950/80 backdrop-blur-md">
                <div className="container mx-auto px-6 h-16 flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <div className="h-8 w-8 bg-emerald-500 rounded-lg flex items-center justify-center">
                            <span className="font-bold text-slate-950">G</span>
                        </div>
                        <span className="text-xl font-bold bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">
                            gstGPT
                        </span>
                    </div>
                    <div className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
                        <Link href="#features" className="hover:text-emerald-400 transition-colors">Features</Link>
                        <Link href="#how-it-works" className="hover:text-emerald-400 transition-colors">How it Works</Link>
                        <Link href="#pricing" className="hover:text-emerald-400 transition-colors">Pricing</Link>
                    </div>
                    <div className="flex items-center gap-4">
                        <Link href="/dashboard/counsel">
                            <Button variant="outline" className="border-slate-700 hover:bg-slate-800 text-slate-300">
                                Log In
                            </Button>
                        </Link>
                        <Link href="/dashboard/counsel">
                            <Button className="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold">
                                Get Started
                            </Button>
                        </Link>
                    </div>
                </div>
            </nav>

            {/* Hero Section */}
            <section className="pt-32 pb-20 md:pt-48 md:pb-32 relative overflow-hidden">
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] bg-emerald-500/20 rounded-full blur-[120px] -z-10" />

                <div className="container mx-auto px-6 text-center">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6 }}
                        className="max-w-4xl mx-auto space-y-8"
                    >
                        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-900 border border-slate-800 text-emerald-400 text-sm font-medium mb-4">
                            <span className="relative flex h-2 w-2">
                                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                                <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                            </span>
                            Now with Agentic Auto-Filing
                        </div>

                        <h1 className="text-5xl md:text-7xl font-bold tracking-tight leading-tight">
                            Your AI-Powered <br />
                            <span className="bg-gradient-to-r from-emerald-400 via-cyan-400 to-blue-500 bg-clip-text text-transparent">
                                GST Counsel & Agent
                            </span>
                        </h1>

                        <p className="text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
                            Stop wrestling with portals and spreadsheets. Let gstGPT analyze your sales, calculate liabilities, and draft your returns automatically.
                        </p>

                        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
                            <Link href="/dashboard/counsel">
                                <Button size="lg" className="h-14 px-8 text-lg bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold rounded-full shadow-[0_0_20px_rgba(16,185,129,0.3)] hover:shadow-[0_0_30px_rgba(16,185,129,0.5)] transition-all">
                                    Start Free Trial <ArrowRight className="ml-2 h-5 w-5" />
                                </Button>
                            </Link>
                            <Button size="lg" variant="outline" className="h-14 px-8 text-lg border-slate-700 hover:bg-slate-800 text-slate-300 rounded-full">
                                Watch Demo
                            </Button>
                        </div>
                    </motion.div>

                    {/* Hero Visual */}
                    <motion.div
                        initial={{ opacity: 0, y: 40 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.3, duration: 0.8 }}
                        className="mt-20 relative max-w-5xl mx-auto"
                    >
                        <div className="absolute -inset-1 bg-gradient-to-r from-emerald-500 to-cyan-500 rounded-xl blur opacity-20" />
                        <div className="relative bg-slate-900 border border-slate-800 rounded-xl shadow-2xl overflow-hidden">
                            <div className="flex items-center gap-2 px-4 py-3 border-b border-slate-800 bg-slate-950/50">
                                <div className="flex gap-1.5">
                                    <div className="w-3 h-3 rounded-full bg-red-500/20 border border-red-500/50" />
                                    <div className="w-3 h-3 rounded-full bg-yellow-500/20 border border-yellow-500/50" />
                                    <div className="w-3 h-3 rounded-full bg-green-500/20 border border-green-500/50" />
                                </div>
                                <div className="mx-auto text-xs font-mono text-slate-500">gstGPT Dashboard</div>
                            </div>
                            <div className="p-2">
                                <img
                                    src="/docs/images/system_architecture.png"
                                    alt="Dashboard Preview"
                                    className="w-full rounded-lg opacity-80 hover:opacity-100 transition-opacity duration-500"
                                />
                                {/* Overlay Mock Chat */}
                                <div className="absolute bottom-8 right-8 w-80 bg-slate-950 border border-slate-700 rounded-lg shadow-2xl p-4 hidden md:block">
                                    <div className="flex items-start gap-3 mb-4">
                                        <div className="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 text-xs">AI</div>
                                        <div className="bg-slate-900 rounded-lg p-3 text-sm text-slate-300">
                                            I've analyzed your October sales. Total liability is ₹45,200. Should I draft GSTR-1?
                                        </div>
                                    </div>
                                    <div className="flex items-center gap-2">
                                        <div className="h-8 flex-1 bg-slate-900 rounded border border-slate-800 px-3 text-xs flex items-center text-slate-500">Yes, draft it...</div>
                                        <div className="h-8 w-8 bg-emerald-500 rounded flex items-center justify-center text-slate-950">
                                            <ArrowRight className="h-4 w-4" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </div>
            </section>

            {/* Features Section */}
            <section id="features" className="py-24 bg-slate-950 relative">
                <div className="container mx-auto px-6">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl md:text-5xl font-bold mb-4">Everything you need to <span className="text-emerald-400">Automate GST</span></h2>
                        <p className="text-slate-400 max-w-2xl mx-auto">Built for CAs, Tax Professionals, and Business Owners who value their time.</p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <FeatureCard
                            icon={<MessageSquare className="h-8 w-8 text-emerald-400" />}
                            title="AI Counsel"
                            description="Ask complex GST questions and get instant, cited answers from our RAG engine trained on the latest Acts."
                        />
                        <FeatureCard
                            icon={<Zap className="h-8 w-8 text-cyan-400" />}
                            title="Agentic Automation"
                            description="Don't just chat—act. The Agent connects to your DB to query sales, reconcile invoices, and draft returns."
                        />
                        <FeatureCard
                            icon={<FileText className="h-8 w-8 text-purple-400" />}
                            title="Auto-Drafting"
                            description="Generate GSTR-1 and GSTR-3B JSONs instantly based on your sales registers. No manual data entry."
                        />
                        <FeatureCard
                            icon={<ShieldCheck className="h-8 w-8 text-blue-400" />}
                            title="Secure & Private"
                            description="Your financial data stays on your infrastructure. Enterprise-grade encryption and access controls."
                        />
                        <FeatureCard
                            icon={<CheckCircle2 className="h-8 w-8 text-orange-400" />}
                            title="Compliance Checks"
                            description="Proactive alerts for deadlines, mismatched ITC, and potential notices before they happen."
                        />
                        <div className="bg-gradient-to-br from-emerald-900/20 to-slate-900 border border-emerald-500/30 rounded-2xl p-8 flex flex-col justify-center items-center text-center group hover:border-emerald-500/50 transition-colors">
                            <h3 className="text-2xl font-bold text-white mb-2">And much more...</h3>
                            <p className="text-slate-400 mb-6">API Integration, Bulk Uploads, Multi-GSTIN support.</p>
                            <Button variant="link" className="text-emerald-400 hover:text-emerald-300 p-0">View all features &rarr;</Button>
                        </div>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="py-24 relative overflow-hidden">
                <div className="absolute inset-0 bg-emerald-900/10" />
                <div className="container mx-auto px-6 relative text-center">
                    <h2 className="text-4xl md:text-6xl font-bold mb-8">Ready to simplify your tax life?</h2>
                    <p className="text-xl text-slate-400 mb-12 max-w-2xl mx-auto">
                        Join thousands of businesses using gstGPT to file returns faster and error-free.
                    </p>
                    <Link href="/dashboard/counsel">
                        <Button size="lg" className="h-16 px-10 text-xl bg-white text-slate-950 hover:bg-slate-200 font-bold rounded-full">
                            Get Started Now
                        </Button>
                    </Link>
                </div>
            </section>

            {/* Footer */}
            <footer className="py-12 border-t border-slate-800 bg-slate-950 text-slate-400 text-sm">
                <div className="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
                    <div className="flex items-center gap-2">
                        <div className="h-6 w-6 bg-emerald-500 rounded flex items-center justify-center">
                            <span className="font-bold text-slate-950 text-xs">G</span>
                        </div>
                        <span className="font-bold text-slate-200">gstGPT</span>
                    </div>
                    <div className="flex gap-8">
                        <a href="#" className="hover:text-emerald-400">Privacy</a>
                        <a href="#" className="hover:text-emerald-400">Terms</a>
                        <a href="#" className="hover:text-emerald-400">Contact</a>
                    </div>
                    <div>
                        &copy; 2024 gstGPT. All rights reserved.
                        <div className="mt-2 text-xs text-slate-500">
                            Created by <a href="https://www.linkedin.com/in/karan-chandra-dey-23392b1b9" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-400 underline decoration-slate-700 underline-offset-4">Karan Chandra Dey</a>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
}

function FeatureCard({ icon, title, description }: { icon: any, title: string, description: string }) {
    return (
        <motion.div
            whileHover={{ y: -5 }}
            className="bg-slate-900/50 border border-slate-800 p-8 rounded-2xl hover:bg-slate-900 hover:border-emerald-500/30 transition-all group"
        >
            <div className="bg-slate-950 w-14 h-14 rounded-xl flex items-center justify-center mb-6 border border-slate-800 group-hover:border-emerald-500/30 transition-colors">
                {icon}
            </div>
            <h3 className="text-xl font-bold text-slate-100 mb-3">{title}</h3>
            <p className="text-slate-400 leading-relaxed">
                {description}
            </p>
        </motion.div>
    );
}
