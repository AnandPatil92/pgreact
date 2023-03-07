// routes
import React, {useState, useEffect} from 'react'
import Router from './routes';
// theme
import ThemeProvider from './theme';
// components
import ScrollToTop from './components/scroll-to-top';
import { StyledChart } from './components/chart';


// ----------------------------------------------------------------------

export default function App() {
    const [data, setData] = useState([{}])
        useEffect(() => {
            fetch("/About").then(
                res => res.json()
            ).then(
                data => {
                    setData(data)
                    console.log(data)
                }
            )
        }, [])
  return (
    <ThemeProvider>
      <ScrollToTop />
      <StyledChart />
      <Router />
    </ThemeProvider>
  );
}
