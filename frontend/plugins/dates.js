export default (context, inject) => {

    const format_date = function(input_date) {

        const monthNames = ["Jan.", "Feb.", "March", "April", "May", "June",
            "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
        ];

        let month = new Date(input_date).getMonth()
        month = monthNames[month]

        let date = new Date(input_date).getDate()

        let year = new Date(input_date).getFullYear()
        
        return `${month} ${date}, ${year}`
    }

    const format_job_date = function(input_date) {

        const monthNames = ["Jan.", "Feb.", "March", "April", "May", "June",
            "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
        ];

        let month = new Date(input_date).getMonth()
        month = monthNames[month]

        let year = new Date(input_date).getFullYear()
        
        return `${month} ${year}`
    }
    
    inject('format_date', format_date)
    inject('format_job_date', format_job_date)
  }