import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "My V0 Project",
  description: "A Next.js project",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
