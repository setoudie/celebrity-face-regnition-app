import { Button, Box, Image, useColorMode, useColorModeValue, Container, Input, Flex, Text } from "@chakra-ui/react";
import { IoMoonSharp } from "react-icons/io5";
import { LuSunMedium } from "react-icons/lu";
import { RiUserSharedFill } from "react-icons/ri";

const Navbar = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  const bg = useColorModeValue("blue.200", "blue.700");
  const inputBg = useColorModeValue("white", "gray.800");
  const textColor = useColorModeValue("green.700", "green.100");

  return (
    <Box
      position="fixed"
      top={0}
      left="50%"
      transform="translateX(-50%)"
      zIndex={1000}
      px={8}
      py={4}
      bg={bg}
      borderRadius="lg"
      boxShadow="lg"
      // w="100%"
      maxW="container.lg"
      display="flex"
      alignItems="center"
      gap={10}
      // justifyContent="space-between"
    >
      <Flex align="center" gap={4}>
        <Text fontSize="38" fontWeight="bold" color={textColor}>
          Face App
        </Text>
        <Button onClick={toggleColorMode} bg="transparent" _hover={{ bg: "transparent" }}>
          {colorMode === 'light' ? <IoMoonSharp size={20} /> : <LuSunMedium size={20} />}
        </Button>
      </Flex>

      <Flex align="center" gap={4}>
        <Input
          placeholder="Recherchez une Célébrité"
          bg={inputBg}
          border="none"
          _placeholder={{ color: "gray.500" }}
          borderRadius="full"
          px={4}
          py={4}
          shadow="sm"
          width="250px"
        />
        <Button colorScheme="teal" borderRadius="full">
          Show All Celebrities
        </Button>
      </Flex>
    </Box>
  );
};

export default Navbar;
