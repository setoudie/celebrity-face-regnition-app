import { useState } from 'react'
import { Stack, HStack, VStack, Box, Flex } from '@chakra-ui/react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Navbar from "./components/Navbar.jsx";
import CelebrityCard from "./components/CelebrityCard.jsx";

import './App.css'

function App() {

  return (
    <Box>
      <Box>
        <Navbar/>
      </Box>
        <CelebrityCard/>
    </Box>

      )
}

export default App;
