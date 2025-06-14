import { Flex, useBreakpointValue } from "@chakra-ui/react"
import { Link } from "@tanstack/react-router"

// import UserMenu from "./UserMenu.tsx"

function Navbar() {
  const display = useBreakpointValue({ base: "none", md: "flex" })

  return (
    <Flex
      display={display}
      justify="space-between"
      position="sticky"
      color="white"
      align="center"
      bg="bg.muted"
      w="100%"
      top={0}
      p={4}
    >
      <Link to="/">Syakyo</Link>
      <Flex gap={2} alignItems="center">
        Menu
        {/* <UserMenu /> */}
      </Flex>
    </Flex>
  )
}

export default Navbar
