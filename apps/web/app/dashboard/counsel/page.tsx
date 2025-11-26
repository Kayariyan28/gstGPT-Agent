"use client"

import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Send, Bot, User, Loader2 } from "lucide-react";
import { ToolWidget } from "@/components/chat/tool-widgets";

interface Message {
    role: "user" | "assistant";
    content: string;
    sources?: string[];
    tool_context?: any;
}

export default function CounselPage() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }, [messages]);

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = input;
        setInput("");
        setMessages((prev) => [...prev, { role: "user", content: userMessage }]);
        setIsLoading(true);

        try {
            const res = await fetch("http://localhost:8000/chat/message", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });
            const data = await res.json();
            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: data.answer,
                    sources: data.sources,
                    tool_context: data.tool_context
                },
            ]);
        } catch (error) {
            setMessages((prev) => [
                ...prev,
                { role: "assistant", content: "Sorry, I encountered an error. Please try again." },
            ]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-[calc(100vh-4rem)]">
            <div className="border-b p-4">
                <h1 className="text-2xl font-bold tracking-tight">AI Counsel & Agent</h1>
                <p className="text-muted-foreground">
                    Ask questions about GST law or manage your returns (e.g., "Draft GSTR-1").
                </p>
            </div>

            <ScrollArea className="flex-1 p-4">
                <div className="space-y-4 max-w-3xl mx-auto">
                    {messages.map((msg, i) => (
                        <div
                            key={i}
                            className={`flex gap-3 ${msg.role === "user" ? "flex-row-reverse" : "flex-row"
                                }`}
                        >
                            <div
                                className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 ${msg.role === "user"
                                        ? "bg-primary text-primary-foreground"
                                        : "bg-muted"
                                    }`}
                            >
                                {msg.role === "user" ? <User size={16} /> : <Bot size={16} />}
                            </div>
                            <div className="flex flex-col max-w-[80%]">
                                <div
                                    className={`rounded-lg p-4 ${msg.role === "user"
                                            ? "bg-primary text-primary-foreground"
                                            : "bg-muted"
                                        }`}
                                >
                                    <div className="whitespace-pre-wrap">{msg.content}</div>

                                    {/* Render Tool Widget if present */}
                                    {msg.tool_context && (
                                        <div className="mt-2">
                                            <ToolWidget context={msg.tool_context} />
                                        </div>
                                    )}

                                    {msg.sources && msg.sources.length > 0 && (
                                        <div className="mt-2 pt-2 border-t border-zinc-200 dark:border-zinc-700">
                                            <p className="text-xs font-semibold mb-1 opacity-70">Sources:</p>
                                            <ul className="list-disc list-inside text-xs opacity-70">
                                                {msg.sources.map((s, idx) => (
                                                    <li key={idx}>{s}</li>
                                                ))}
                                            </ul>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                    {isLoading && (
                        <div className="flex gap-3">
                            <div className="w-8 h-8 rounded-full bg-muted flex items-center justify-center shrink-0">
                                <Bot size={16} />
                            </div>
                            <div className="bg-muted rounded-lg p-4 flex items-center">
                                <Loader2 className="h-4 w-4 animate-spin mr-2" />
                                <span className="text-sm">Thinking...</span>
                            </div>
                        </div>
                    )}
                    <div ref={scrollRef} />
                </div>
            </ScrollArea>

            <div className="p-4 border-t bg-background">
                <div className="max-w-3xl mx-auto flex gap-2">
                    <Input
                        placeholder="Ask a question or give a command..."
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                    />
                    <Button onClick={sendMessage} disabled={isLoading}>
                        <Send size={16} />
                    </Button>
                </div>
            </div>
        </div>
    );
}
