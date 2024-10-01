import { Card, CardHeader, CardBody, CardFooter, Avatar, Flex, Box, Heading, Text, IconButton, Button, Image } from '@chakra-ui/react';
import { BsThreeDotsVertical } from 'react-icons/bs';
import { BiLike, BiChat, BiShare } from 'react-icons/bi';

const CelebrityCard = () => {
    return (
        <Card maxW='md'>
            <CardHeader>
                <Flex spacing='4'>
                    <Flex minWidth='max-content' flex='1' gap='4' alignItems='center' flexWrap='wrap'>
                        <Image
                            borderRadius='full'
                            boxSize='250px'
                            src='https://imgs.search.brave.com/FNk2ZgdV4J_UWk4go4WGDkxnvCR-Sxu5GuR0MxUgZSM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9oaXBz/LmhlYXJzdGFwcHMu/Y29tL2htZy1wcm9k/L2ltYWdlcy93aWxs/LXNtaXRoLWF0dGVu/ZHMtdmFyaWV0eXMt/Y3JlYXRpdmUtaW1w/YWN0LWF3YXJkcy1h/bmQtMTAtZGlyZWN0/b3JzLXRvLXdhdGNo/LWJydW5jaC1hdC10/aGUtcGFya2VyLXBh/bG0tc3ByaW5ncy1v/bi1qYW51YXJ5LTMt/MjAxNi1pbi1wYWxt/LXNwcmluZ3MtY2Fs/aWZvcm5pYS1waG90/by1ieS1qZXJvZC1o/YXJyaXNnZXR0eS1p/bWFnZXMuanBnP2Ny/b3A9MXh3OjEuMHho/O2NlbnRlcix0b3Am/cmVzaXplPTY0MDoq'
                            alt='Will Smith'
                        />
                    </Flex>
                </Flex>
            </CardHeader>

            <CardBody>
                <Box>
                    <Heading size='sm'>Will Smith</Heading>
                    <Text>American Actor</Text>
                </Box>
            </CardBody>


        </Card>
    );
};
export default CelebrityCard;
