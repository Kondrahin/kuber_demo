import './MyEventInfo.css'
import { useAsync } from "react-async";


async function getEvent({ data }) {

    let eventInfo = data
    let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    let event_datetime = new Date(eventInfo.event_datetime)


    return (
        <div>
            <div className="position-static">
                <div className="position-absolute start-50 p-5 translate-middle-x">
                    <h1 className="display-1">{eventInfo.title}</h1>
                </div>
                <div className="description">
                    <p className="lead">
                        {eventInfo.description}
                    </p>
                </div>
                <div className="position-absolute top-50 start-50 translate-middle-x">
                    <h6 className="lead"><b>Место проведения:</b> {eventInfo.location} <br /></h6>
                    <h6 className="lead"><b>Дата проведения:</b> {event_datetime.toLocaleDateString("ru", options)}</h6>
                </div>
            </div>
        </div>
    );
}


const MyEventInfo = ({ eventData }) => {

    const { data, error, isPending } = useAsync({
        promiseFn: getEvent,
        data: eventData,
    })

    if (isPending) return "Loading..."
    if (data) {
        return (
            <div>
                {data}
            </div>
        );
    }
    return null
};

export default MyEventInfo;
