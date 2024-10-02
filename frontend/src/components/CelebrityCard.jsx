import { Card, CardHeader, CardBody, CardFooter, Avatar, Flex, Box, Heading, Text, IconButton, Button, Image } from '@chakra-ui/react';

const CelebrityCard = ({name, surname, profession, imageUrl}) => {

    return (
        <Card maxW='md'>
            <CardHeader>
                <Flex minWidth='max-content' flex='1' gap='4' alignItems='center' flexWrap='wrap'>
                    <Image
                        borderRadius='100%'
                        boxSize='150px'
                        src={imageUrl}
                        alt={name}
                    />
                </Flex>
            </CardHeader>

            <CardBody>
                <Box>
                    <Heading size='sm'>{name} {surname}</Heading>
                    <Text>{profession}</Text>
                </Box>
            </CardBody>

        </Card>
    );
};
export default CelebrityCard;
